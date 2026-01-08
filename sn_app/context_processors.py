"""
Context Processors
Make cart available in all templates
"""

from .cart import Cart


def cart(request):
    """
    Add cart to template context globally
    
    Usage in templates:
    {{ cart|length }} - number of items
    {{ cart.get_total_price }} - total price
    """
    return {
        'cart': Cart(request)
    }
