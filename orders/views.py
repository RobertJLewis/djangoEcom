from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse
from django.views.decorators.http import csrf_exempt, requires_http_methods
from django.http import HttpResponse, HttpResponseBadRequest
from decimal import Decimal
import stripe 

from cart.cart import Cart
from .models import Order, OrderItem

stripe.api_key = settings.STRIPE_SECRET_KEY

FLAT_SHIPPING_FEE = Decimal('3.00')
@requires_http_methods(["GET", "POST"])
def checkout_view(request):
    """
    View to display the checkout page and handle the checkout process.
    """
    cart = Cart(request)
    shipping_fee=FLAT_SHIPPING_FEE if len(cart) else Decimal('0.00')
    total_with_shipping = cart.get_total_price + shipping_fee

    return render(request, 'orders/checkout.html', {
        'cart': cart,
        'shipping_fee': shipping_fee,
        'total_with_shipping': total_with_shipping,
    })

@requires_http_methods(["POST"])
def strt_checkout(request):
    cart= Cart(request)
    if len(cart) == 0:
        return HttpResponseBadRequest("Your cart is empty.")
    
    email = request.POST.get('email').strip()
    order= Order.objects.create(
        user=request.user if request.user.is_authenticated else None,
        email=email or (getattr(request.user, 'email', '') if request.user.is_authenticated else ''),
        first_name=request.POST.get('first_name', '').strip(),
        last_name=request.POST.get('last_name', '').strip(),
        address=request.POST.get('address', '').strip(),
        city=request.POST.get('city', '').strip(),
        country=request.POST.get('country', '').strip(),
        postcode=request.POST.get('postcode', '').strip(),
        total_cents=int((cart.get_total_price + FLAT_SHIPPING_FEE) * 100),
        curecncy='GBP',
    )

    for item in cart:
        OrderItem.objects.create(
            order=order,
            product_title=item['product'].name,
            quantity=item['quantity'],
            unit_price_cents=int(item['unit_price'] * 100),    
        )

    line_itmes = [
        {
            'price_data': {
                'currency': 'gbp',
                'product_data': {
                    'name': item['product'].name,
                },
                'unit_amount': int(item['unit_price'] * 100),
            },
            'quantity': item['quantity'],
        } for item in cart
    ]
    if FLAT_SHIPPING_FEE:
        line_itmes.append({
            'price_data': {
                'currency': 'gbp',
                'product_data': {
                    'name': 'Shipping Fee',
                },
                'unit_amount': int(FLAT_SHIPPING_FEE * 100),
            },
            'quantity': 1,
        })

    success_url = request.build_absolute_uri(reverse('orders:checkout_success')) + '?session_id={CHECKOUT_SESSION_ID}'
    cancel_url = request.build_absolute_uri(reverse('orders:checkout_cancel'))

    session = stripe.checkout.Session.create(
        mode='payment',
        line_items=line_itmes,
        customer_email=order.email,
        success_url=success_url,
        cancel_url=cancel_url,
        shipping_address_collection={
            'allowed_countries': ['GB', 'US', 'CA', 'AU'],
        },
        metadata={
            'order_id': order.id,
        }  
    )

    order.stripe_session_id = session.id
    order.save(update_fields=['stripe_session_id'])

    return redirect(session.url, permanent=False)

def checkout_success(request):
    return render(request, 'orders/checkout_success.html')

def checkout_cancelled(request):
    return render(request, 'orders/checkout_cancelled.html')

@csrf_exempt
@requires_http_methods(["POST"])
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponseBadRequest()
    except stripe.error.SignatureVerificationError as e:
        return HttpResponseBadRequest()

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        order=Order.objects.filter(stripe_session_id=session.get('id')).first()
        if order and order.status != Order.Status.PAID:
            order.status = Order.Status.PAID
            order.save(update_fields=['status'])

    return HttpResponse(status=200)



    