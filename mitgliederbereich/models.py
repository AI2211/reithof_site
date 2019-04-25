from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


class nameMistplan(models.Model):
    user = models.ForeignKey(
        get_user_model(),related_name='dienste', on_delete=models.CASCADE
    )
    date = models.DateField()
    horsepower = models.IntegerField()
