from django.contrib import admin
from .models import Profile, Pferd, Eintrag, Kurs, Kategorie
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from .forms import ProfileForm, ProfileChangeForm
from django.contrib.auth.admin import UserAdmin

class ProfileAdmin(UserAdmin):
    add_form = ProfileForm
    form = ProfileChangeForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Persönliche Daten'), {'fields': ('vorname', 'nachname', 'email', 'mistpunkte')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'vorname', 'nachname', 'password1', 'password2')}
        ),
    )

    list_display = ('email', 'vorname', 'nachname', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'vorname', 'nachname', 'email')
    ordering = ('nachname',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Pferd)
admin.site.register(Eintrag)
admin.site.register(Kurs)
admin.site.register(Kategorie)
admin.site.unregister(Group)
