from django.test import TestCase
from .models import Ticket
from .forms import TicketForm

# Create your tests here

# Models test
class TicketTests(TestCase):
    """
    Here we will define the tests that will run against the Ticket models
    """
    def create_ticket(self, issue_type="Bug", issue_name="Test", issue_detail="Large", status="Doing",
                            urgent="True"):
                                return Ticket.objects.create(issue_type=issue_type, issue_name=issue_name, issue_detail=issue_detail, status=status, urgent=True)

    def test_ticket_creation(self):
        t = self.create_ticket()
        self.assertTrue(isinstance(t, Ticket))
        self.assertEqual(t.issue_type)
        
# Forms test
        
    def test_invalid_form(self):
        t = Ticket.objects.create(issue_type="Bug", issue_name="Test", issue_detail="large", status="Doing", urgent=False)
        data = {'issue_type': t.issue_detail, 'issue_name': t.issue_name, 'issue_detail': t.issue_detail, 'status': t.status, 'urgent': False}
        form = TicketForm(data=data)
        self.assertFalse(form.is_valid())
