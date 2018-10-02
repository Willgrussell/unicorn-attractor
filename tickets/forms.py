from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = (  'issue_type',
                    'issue_name', 
                    'issue_detail',
                    'status',
                    'due_date',
                    'urgent',
                    'published_date', 
                    'image',
                    'tag')