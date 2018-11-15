from django.conf.urls import url
from .views import promotion, issue_chart, status_chart, urgent_chart, not_urgent_chart

urlpatterns = [
    url(r'^$', promotion, name="promotion"),
    url(r'^api/issue', issue_chart, name="issue_chart"),
    url(r'^api/status', status_chart, name="status_chart"),
    url(r'^api/urgent', urgent_chart, name="urgent_chart"),
    url(r'^api/noturgent', not_urgent_chart, name="not_urgent_chart")
    ]