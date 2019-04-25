from . import views
from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'profil/', views.profil, name='profil'),



    path(r'delete_profil/<int:pk>/', views.profile_delete, name='delete_profil'),
    path(r'activate_profil/<int:pk>/', views.profile_set_active, name='activate_profile'),
    path(r'deactivate_profil/<int:pk>/', views.profile_set_not_active, name='deactivate_profile'),
    path(r'staff_profil/<int:pk>/', views.profile_set_staff, name='staff_profile'),
    path(r'not_staff_profil/<int:pk>/', views.profile_set_not_staff, name='not_staff_profile'),

    path(r'email-change/', views.email_change, name='email_change'),
    path(r'email-change-done/', views.email_change_done, name='email_change_done'),

    path(r'management/', views.pferde_management, name='pferde_management'),
    path(r'standort/<int:pk>/', views.pferd_standort, name='pferd_standort'),
    path(r'meine-kurse/', views.meine_kurse, name='meine_kurse'),


    path(r'password-change/', auth_views.PasswordChangeView.as_view(template_name='mitgliederbereich/password_change.html'), name='password_change'),

    path(r'password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='mitgliederbereich/password_change_done.html'), name='password_change_done'),

    path(r'edit-profil/', views.edit_profil, name='edit_profil'),

    path(r'edit-profil-success/', views.edit_profil, name='edit_profil_success'),

    path(r'calendar', views.CalendarView.as_view(), name='calendar'),
    path(r'mistplan', views.MistplanView.as_view(), name='mistplan'),
    path(r'mistplan/<str:date>/<int:horsePower>', views.MistplanDetail.as_view()),
    path(r'event/new', views.event, name='event_new'),
	path(r'event/edit/<event_id>/', views.event, name='event_edit'),


]