from django.test import TestCase
from .models import Ticket

# Create your tests here

# Models test
class TicketTests(TestCase):
    """
    Here we will define the tests that will run against the Ticket models
    """
    def test_str(self):
        test_issue_name = Ticket(issue_name='issue with site')
        self.assertEqual(str(test_issue_name), 'issue with site')

