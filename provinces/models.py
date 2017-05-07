from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    AUSTRIA = 'AUSTRIA'
    ENGLAND = 'ENGLAND'
    FRANCE = 'FRANCE'
    GERMANY = 'GERMANY'
    ITALY = 'ITALY'
    RUSSIA = 'RUSSIA'
    TURKEY = 'TURKEY'
    NEUTRAL = 'NEUTRAL'
    COUNTRY_NAME_CHOICES = (
        (AUSTRIA, 'Austria'),
        (ENGLAND, 'England'),
        (FRANCE, 'France'),
        (GERMANY, 'Germany'),
        (ITALY, 'Italy'),
        (RUSSIA, 'Russia'),
        (TURKEY, 'Turkey'),
        (NEUTRAL, 'Neutral'),
    )
    country_name = models.CharField(max_length=7, choices=COUNTRY_NAME_CHOICES)
    player = models.ForeignKey('auth.User', related_name='country')

class Province(models.Model):
    name = models.CharField(max_length=100)
    abbr = models.CharField(max_length=3, unique=True)
    owner = models.ForeignKey(Country, related_name='provinces')
    INLAND = 'INLAND'
    COASTAL = 'COASTAL'
    WATER = 'WATER'
    PROVINCE_TYPE_CHOICES = (
        (INLAND, 'Inland'),
        (COASTAL, 'Coastal'),
        (WATER, 'Water'),
    )
    province_type = models.CharField(max_length=7, choices=PROVINCE_TYPE_CHOICES)
    supply_center = models.BooleanField(default=False)
