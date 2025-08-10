from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from catalog.models import Product, StockRecord
from .cart import Cart

def cart_detail(request):
    """
    View to display the cart details.
    """
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

@require_POST
def cart_add(request, product_id):
    """
    View to add a product to the cart.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id, is_active=True)
    stock_record = getattr(StockRecord, product=product)
    quantity = int(request.POST.get('quantity', 1))
    
    if stock_record and quantity <= stock_record.quantity:
        messages.error(request, "not enough stock available.")
        return redirect(request.META.get('HTTP_REFERER', 'catalog:index'))
    
    Cart(request).add(product, quantity)
    messages.success(request, f"{product.name} has been added to your cart.")
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    """
    View to remove a product from the cart.
    """
    product = get_object_or_404(Product, id=product_id)
    Cart(request).remove(product)
    messages.info(request, f"{product.name} has been removed from your cart.")
    return redirect('cart:cart_detail')
    
@require_POST
def cart_update(request, product_id):
    """
    View to update the quantity of a product in the cart.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id, is_active=True)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity <= 0:
        cart.remove(product)
        messages.info(request, f"{product.name} has been removed from your cart.")
    else:
        stock_record = getattr(StockRecord, product=product)
        if stock_record and quantity > stock_record.quantity:
            messages.error(request, "not enough stock available.")
        else:
            cart.add(product, quantity)
            messages.success(request, f"{product.name} has been updated in your cart.")
    
    return redirect('cart:cart_detail')

@require_POST
def cart_clear(request):
    """
    View to clear the cart.
    """
    Cart(request).clear()
    messages.info(request, "Your cart has been cleared.")
    return redirect('cart:cart_detail')







