from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^(?P<type>[a-z]+)/$', views.transaction, name="transaction_table"),
    url(r'^(?P<hash>[A-Za-z0-9_]+)/$', views.tx_detail, name="transaction_details"),
]
