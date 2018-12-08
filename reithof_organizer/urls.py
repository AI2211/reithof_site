from . import views
from django.conf.urls import url

urlpatterns = [
    #Unser Stall
    url(r'^$', views.index, name='unser_stall'),
    #Über Uns
    url(r'^ueberuns/$', views.ueber_uns, name='ueber_uns'),
    #Aktuell
    url(r'^aktuell/$', views.aktuell, name='aktuell'),
    #Galerie
    url(r'^galerie/$', views.galerie, name='galerie'),
    #Unsere Pferde
    url(r'^unsere_pferde/$', views.unsere_pferde, name='unsere_pferde'),
]
