from django.db import models
from django.contrib.auth.models import User

from provinces.config import COUNTRY_CHOICES, PROVINCE_TYPE_CHOICES

class Country(models.Model):
    country_name = models.CharField(max_length=7, choices=COUNTRY_CHOICES)
    player = models.ForeignKey('auth.User', related_name='country')

class Province(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=3, unique=True)
    owner = models.ForeignKey(Country, related_name='provinces')
    province_type = models.CharField(max_length=7, choices=PROVINCE_TYPE_CHOICES)
    supply_center = models.BooleanField(default=False)
