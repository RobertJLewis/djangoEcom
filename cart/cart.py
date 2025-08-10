from decimal import Decimal
from django.conf import settings 
from catalog.models import Product

CART_SESSION_ID = 'cart'

class Cart:
    """
    A class to manage the shopping cart in the session.
    """
    def __init__(self, request):
        self.session = request.session
        self.key = getattr(settings, 'CART_SESSION_ID', 'cart')
        cart = self.session.get(self.key)
        if not cart:
            cart = self.session[self.key] = {}
        self.cart = cart

    def __len__(self):
        """
        Return the total number of items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def __iter__(self):
        """
        Iterate over the items in the cart.
        """
        product_ids = [int(product_id) for product_id in self.cart.keys()]
        products = {product.id : product for product in Product.objects.filter(id__in=product_ids)}
    
        for product_id, item in self.cart.items():
            product = products.get(int(product_id))
            unit_price = item['price']
            yield {
                'product': product,
                'quantity': item['quantity'],
                'unit_price': Decimal(unit_price),
            }

    def add(self, product, quantity=1):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """
        Save the current state of the cart in the session.
        """
        self.session.modified = True

    @property
    def get_total_price(self):
        """
        Calculate the total price of all items in the cart.
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        """
        Clear the cart.
        """
        del self.session[self.key]
        self.save()
