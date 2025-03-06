from django.db import models

# Create your models here.

class Stations(models.Model):
    station = models.CharField(max_length=42)
    def __str__(self):
        return self.station

class KLM(models.Model):
    klm = models.FloatField()


class UserDetails(models.Model):
    mail = models.CharField(max_length=32)
    from_station = models.CharField(max_length=42)
    to_station = models.CharField(max_length=42)

