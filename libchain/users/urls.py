from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.login, name="login"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^edit/$', views.edit, name="edit"),
    url(r'^logout/$', views.logout, name="logout"),

    url(r'^admin/dashboard/$', views.dashboard, name="dashboard"),

    url(r'^details/(?P<libcard>[0-9]+)/$', views.student_details, name="student_details"),
    url(r'^details/$', views.student_search, name="student_search"),
]
