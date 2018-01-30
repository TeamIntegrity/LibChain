from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', views.login, name="login"),
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^edit/$', views.edit, name="edit"),
    url(r'^logout/$', views.logout, name="logout"),

    url(r'^admin/dashboard/$', views.dashboard, name="dashboard"),

    url(r'^details/(?P<libcard>[0-9]+)/$', views.user_detail, name="user_detail"),
]
