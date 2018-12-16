from django.contrib import admin
from .models import Profile, Pferd
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from .forms import ProfileForm, ProfileChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import Profile

class ProfileAdmin(UserAdmin):
    add_form = ProfileForm
    form = ProfileChangeForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Persönliche Daten'), {'fields': ('vorname', 'nachname', 'email', 'geburtsdatum', 'mistpunkte', 'pferd')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'vorname', 'nachname', 'password1', 'password2', 'geburtsdatum')}
        ),
    )

    list_display = ('email', 'vorname', 'nachname', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'vorname', 'nachname', 'email')
    ordering = ('nachname',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Pferd)
admin.site.unregister(Group)