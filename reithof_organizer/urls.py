from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    #Unser Stall
    path(r'', views.index, name='ritterstall'),
    #Über Uns
    path(r'ueberuns/', views.ueber_uns, name='ueber_uns'),
    #reithof.de/aktuell/
    path(r'kurse/', views.kurse, name='kurse'),
    path(r'news/', views.news, name='news'),
    #Galerie
    path(r'galerie/', views.galerie, name='galerie'),
    #Unsere Pferde
    path(r'unsere_pferde/', views.unsere_pferde, name='unsere_pferde'),
    #Kontakt
    path(r'kontakt/', views.kontakt, name='kontakt'),
    #Impressum
    path(r'impressum/', views.impressum, name='impressum'),
    # Registrierung
    path(r'register/', views.register, name='register'),
    # Login
    path(r'login/', auth_views.LoginView.as_view(template_name='reithof_organizer/login.html'), name='login'),
    # Logout
    path(r'logout/', auth_views.LogoutView.as_view(template_name='reithof_organizer/logout.html'), name='logout'),
    # Passwort zurücksetzen
    path(r'password-reset/', auth_views.PasswordResetView.as_view(template_name='reithof_organizer/password_reset.html'), name='password_reset'),
    # Passwort zurückgesetzt
    path(r'password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='reithof_organizer/password_reset_done.html'), name='password_reset_done'),
    # Passwort Reset bestätigt
    path(r'password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reithof_organizer/password_reset_confirm.html'), name='password_reset_confirm'),

    path(r'password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reithof_organizer/password_reset_complete.html'), name='password_reset_complete'),

    path(r'delete_kurs/<int:pk>/', views.delete_kurs, name='delete_kurs'),
    path(r'delete_news/<int:pk>/', views.delete_news, name='delete_news'),

    path(r'add-user-kurs/<int:pk>', views.eintragen_kurs, name='eintragen_kurs'),
    path(r'remove-user-kurs/<int:pk>', views.austragen_kurs, name='ausgetragen_kurs'),

    path(r'leaflet', views.leaflet_test, name='leaflet')
]