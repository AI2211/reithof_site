from django.contrib import admin
from .models import Profile, Pferd
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'is_bot_flag', 'password1', 'password2')}
        ),
    )



admin.site.register(Profile, UserAdmin)
admin.site.register(Pferd)
admin.site.unregister(Group)

# class ProfileCreationForm(UserCreationForm):
#     password1 = forms.CharField(label='Passwort', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Passwort bestätigen', widget=forms.PasswordInput)
#
#     class Meta:
#         model = Profile
#         fields = ['vorname', 'nachname', 'email', 'geburtsdatum', 'password1', 'password2']