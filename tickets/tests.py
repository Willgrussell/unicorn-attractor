from django.test import TestCase
from .models import Ticket

# Create your tests here.
class TicketTests(TestCase):
    """
    Defining a test that will run against my Ticket model
    """
    def test_str(self):
        test_status = Ticket(status='ToDo')
        self.assertEqual(str(test_status), 'ToDo')