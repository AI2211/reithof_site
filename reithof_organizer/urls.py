from . import views
from django.conf.urls import url

urlpatterns = [
    #Unser Stall
    url(r'^$', views.index, name='ritterstall'),
    #Über Uns
    url(r'^ueberuns/$', views.ueber_uns, name='ueber_uns'),
    #reithof.de/aktuell/
    url(r'^kurse/$', views.kurse, name='kurse'),
    #Galerie
    url(r'^galerie/$', views.galerie, name='galerie'),
    #Unsere Pferde
    url(r'^unsere_pferde/$', views.unsere_pferde, name='unsere_pferde'),
    #Facebooknews
    url(r'^facebooknews/$', views.facebooknews, name='facebook')
]
