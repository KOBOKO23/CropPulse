# agro2_form.py
from django.db import models
from .base import BaseAgroModel


class Agro2(BaseAgroModel):
    # Phenological Observation fields
    date_of_observation = models.DateField()
    phenological_phase = models.CharField(max_length=100)
    development_phase = models.CharField(max_length=100)  # specific Agro2
    number_of_trees_with_features = models.IntegerField()

    # Field Work notes (up to 3 fields, with flexibility)
    field_work_1 = models.TextField(blank=True, null=True)
    field_work_2 = models.TextField(blank=True, null=True)
    field_work_3 = models.TextField(blank=True, null=True)

    # Custom notes field for additional observations
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Agro2 Report for {self.crop} in {self.district}, {self.year}"
