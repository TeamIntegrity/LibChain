from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^semester/(?P<sem>[0-9]+)/$', views.by_semester, name="books_by_sems"),
    url(r'^branch/(?P<b>[a-z]+)/$', views.by_branch, name="books_by_branch"),
    url(r'^subject/(?P<sub>[a-z]+)/$', views.by_subject, name="books_by_sub"),

    url(r'^(?P<id>[0-9]+)/$', views.description, name="books_description"),
]
