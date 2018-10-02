from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Ticket
from .forms import TicketForm

def all_tickets(request):
    """
    Creates a view that returns a list of tickets published till now
    and render them to the 'tickets.html' template
    """
    tickets = Ticket.objects.all()
    return render(request, "tickets.html", {'tickets': tickets})
    
def ticket_detail(request, pk):
    """
    Creates a view that returns a single ticket object based on the ticket ID (PK)
    and renders it to the 'ticketdetail.html' or will return error if its not found
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.views += 1
    ticket.save()
    return render(request, "ticketdetail.html", {'ticket': ticket})

def create_or_edit_ticket(request, pk=None):
    """
    Creates a view that allows us to create or edit a ticket depending on if the ticket ID 
    is known or not
    """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = form.save()
            return redirect(ticket_detail, ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'ticketform.html', {'form': form})