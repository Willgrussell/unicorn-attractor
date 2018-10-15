from django.shortcuts import render
from tickets.models import Ticket

# Create your views here.
def do_search(request):
    """
    Filtering all tickets in database and return them to views
    """
    tickets = Ticket.objects.filter(issue_type__icontains=request.GET['q'])
    return render(request, 'tickets.html', {"tickets":tickets})