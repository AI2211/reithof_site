from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^reithof/', include('reithof_organizer.urls')),
    url(r'^mitglieder/', include('mitgliederbereich.urls')),
    url(r'^admin/', admin.site.urls),
]
