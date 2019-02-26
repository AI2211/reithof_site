from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    #Unser Stall
    url(r'^$', views.index, name='ritterstall'),
    #Über Uns
    url(r'^ueberuns/$', views.ueber_uns, name='ueber_uns'),
    #reithof.de/aktuell/
    url(r'^kurse/$', views.kurse, name='kurse'),
    url(r'^news/$', views.news, name='news'),
    #Galerie
    url(r'^galerie/$', views.galerie, name='galerie'),
    #Unsere Pferde
    url(r'^unsere_pferde/$', views.unsere_pferde, name='unsere_pferde'),
    #Kontakt
    url(r'^kontakt/$', views.kontakt, name='kontakt'),
    #Impressum
    url(r'^impressum/$', views.impressum, name='impressum'),
    # Registrierung
    url(r'^register/$', views.register, name='register'),
    # Login
    url(r'^login/$', auth_views.LoginView.as_view(template_name='reithof_organizer/login.html'), name='login'),
    # Logout
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='reithof_organizer/logout.html'), name='logout')
]
