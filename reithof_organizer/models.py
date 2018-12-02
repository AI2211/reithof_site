from django.db import models

class Person(models.Model):
    pferd = models.ForeignKey(on_delete=models.DO_NOTHING)
    vorname = models.CharField(max_length=100)
    nachname = models.CharField(max_length=100)
    geburtstag = models.DateTimeField(blank=True)
    erstellt_am = models.DateTimeField(auto_now_add=True)
    mistpunkte = models.IntegerField()

class Pferd(models.Model):
    offizieller_name = models.CharField(max_length=100)
    rufname = models.CharField(max_length=100)
    geburtstag = models.DateTimeField(blank=True)
    kategorie = models.CharField(max_length=100)

