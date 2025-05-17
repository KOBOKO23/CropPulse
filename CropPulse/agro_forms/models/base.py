# base.py
from django.db import models


class BaseAgroModel(models.Model):
    # Common fields
    country = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    station = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    crop = models.CharField(max_length=100)
    variety = models.CharField(max_length=100)
    date_of_sowing = models.DateField()
    observer_name = models.CharField(max_length=100)

    # Additional fields for Agro3 and specific forms
    year_of_planting = models.IntegerField(null=True, blank=True)  # For Agro3
    number_of_plants_observed = models.IntegerField(null=True, blank=True)  # 3
    date_of_observation = models.DateField(null=True, blank=True)  # Agro3-2

    class Meta:
        abstract = True
