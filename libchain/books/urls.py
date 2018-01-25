from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^semester/(?P<sem>[0-9]+)/$', views.by_semester, name="books_by_sems"),
    url(r'^branch/(?P<b>[-\w\s]+)/$', views.by_branch, name="books_by_branch"),
    url(r'^subject/(?P<sub>[-\w\s]+)/$', views.by_subject, name="books_by_sub"),

    url(r'^(?P<id>[0-9]+)/$', views.description, name="books_description"),
    url(r'^search/$', views.search, name="search"),

    url(r'^add/$', views.add_books, name="add_books"),

    url(r'^issue/$', views.issue, name="issue_books"),
    url(r'^issue/confirm/$', views.issue_confirm, name="issue_books_confirm"),

    url(r'^return/$', views.return_book, name="return_books"),
    url(r'^return/confirm/$', views.return_confirm, name="return_books_confirm"),
]
