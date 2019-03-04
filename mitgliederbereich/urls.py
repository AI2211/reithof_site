from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profil/$', views.profil, name='profil'),



    url(r'^delete_profil/(?P<pk>[0-9]+)/$', views.profile_delete, name='delete_profil'),
    url(r'^activate_profil/(?P<pk>[0-9]+)/$', views.profile_set_active, name='activate_profile'),
    url(r'^deactivate_profil/(?P<pk>[0-9]+)/$', views.profile_set_not_active, name='deactivate_profile'),
    url(r'^staff_profil/(?P<pk>[0-9]+)/$', views.profile_set_staff, name='staff_profile'),
    url(r'^not_staff_profil/(?P<pk>[0-9]+)/$', views.profile_set_not_staff, name='not_staff_profile'),

]