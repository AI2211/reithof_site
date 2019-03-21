# Generated by Django 2.1.4 on 2019-03-01 13:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, verbose_name='Username')),
                ('vorname', models.CharField(blank=True, max_length=50, verbose_name='Vorname')),
                ('nachname', models.CharField(blank=True, max_length=50, verbose_name='Nachname')),
                ('password', models.CharField(max_length=128, verbose_name='Passwort')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Letzte Anmeldung')),
                ('email', models.EmailField(error_messages={'unique': 'Ein Nutzer mit dieser E-Mail-Adresse existiert bereits!'}, max_length=254, unique=True, verbose_name='Email-Adresse')),
                ('geburtsdatum', models.DateField(null=True, verbose_name='Geburtsdatum')),
                ('mistpunkte', models.IntegerField(null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Erstellt am')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='aktiv')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Mitglied',
                'verbose_name_plural': 'Mitglieder',
            },
        ),
        migrations.CreateModel(
            name='Eintrag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=250)),
                ('nachricht', models.TextField()),
                ('erstellt_am', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Erstellt am')),
                ('kategorie', models.CharField(max_length=100)),
                ('bild', models.ImageField(blank=True, upload_to='')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Eintrag',
                'verbose_name_plural': 'Einträge',
            },
        ),
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('beschreibung', models.CharField(max_length=200)),
                ('bild', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Kurs',
                'verbose_name_plural': 'Kurse',
            },
        ),
        migrations.CreateModel(
            name='Pferd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offizieller_name', models.CharField(max_length=100)),
                ('rufname', models.CharField(max_length=100)),
                ('geburtstag', models.DateTimeField(blank=True)),
                ('kategorie', models.CharField(max_length=100)),
                ('besitzer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pferd',
                'verbose_name_plural': 'Pferde',
            },
        ),
    ]
