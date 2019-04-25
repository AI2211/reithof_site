# Generated by Django 2.1.4 on 2019-04-25 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reithof_organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('long', models.IntegerField(blank=True)),
                ('lat', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'Kategorie',
                'verbose_name_plural': 'Kategorien',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='Kurse',
            field=models.ManyToManyField(to='reithof_organizer.Kurs'),
        ),
        migrations.AlterField(
            model_name='pferd',
            name='kategorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reithof_organizer.Kategorie'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='geburtsdatum',
            field=models.DateField(blank=True, null=True, verbose_name='Geburtsdatum'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mistpunkte',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=150, verbose_name='Username'),
        ),
    ]
