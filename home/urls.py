from django.conf.urls import url, include
from .views import index, contact, about

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^about/$', about, name="about"),
    url(r'^contact/$', contact, name="contact"),
    ]