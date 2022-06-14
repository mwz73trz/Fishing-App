from django.db import models
from django.utils import timezone

class Event(models.Model):
    date = models.DateField(auto_now_add=True)
    place = models.CharField(max_length=50)
    water = models.CharField(max_length=25)
    temperature = models.CharField(max_length=10)
    sky = models.CharField(max_length=25)
    wind = models.CharField(max_length=25)
    water = models.CharField(max_length=25)
    type_fishing = models.CharField(max_length=25)
    note = models.TextField()

    def __str__(self):
        return f'{self.date}'
