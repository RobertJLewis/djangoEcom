from .cart import Cart 

def cart(request):
    """
    Context processor to add the cart to the context.
    """
    return {'cart': Cart(request)}
    
