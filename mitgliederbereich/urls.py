from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='profil'),

    #Mistplan
    url(r'^mistplan/$', views.mistplan, name='mistplan'),

    #StandortPferde
    url(r'^standortPferde/$', views.standortPferde, name='standortPferde'),

    #Termine
    url(r'^termine/$', views.termine, name='termine'),

]