from django.test import TestCase
from .models import Ticket
from .forms import TicketForm

# Create your tests here

# Models test
class TicketTests(TestCase):
    """
    Here we will define the tests that will run against the Ticket models
    """
    def test_str(self):
        test_issue_name = Ticket(issue_name='issue with site')
        self.assertEqual(str(test_issue_name), 'issue with site')
        
# Forms test
        
    def test_invalid_form(self):
        t = Ticket.objects.create(issue_type="Bug", issue_name="Test", issue_detail="large", status="Doing", urgent=False)
        data = {'issue_type': t.issue_detail, 'issue_name': t.issue_name, 'issue_detail': t.issue_detail, 'status': t.status, 'urgent': False}
        form = TicketForm(data=data)
        self.assertFalse(form.is_valid())
