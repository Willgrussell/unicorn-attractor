from django.shortcuts import get_object_or_404
from tickets.models import Ticket

def cart_contents(request):
    """
    Ensures the cart contents are available when rendering every page
    """
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    ticket_count = 0
    for id, quantity in cart.items():
        ticket = get_object_or_404(Ticket, pk=id)
        total += quantity * ticket.price
        ticket_count += quantity
        cart_items.append({'id':id, 'quantity': quantity, 'ticket': ticket})
        
    return { 'cart_items':cart_items, 'total':total, 'ticket_count': ticket_count }