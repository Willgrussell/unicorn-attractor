from django.conf.urls import url, include
from home.views import index, contact, about, promotion

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^about/$', about, name="about"),
    url(r'^contact/$', contact, name="contact"),
    url(r'^promotion/$', promotion, name="promotion"),
    ]