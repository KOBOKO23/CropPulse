# agro3_form.py
from django.db import models
from .base import BaseAgroModel


class Agro3(BaseAgroModel):

    # Plant-specific phenological phase observation for up to 10 plants
    phenological_phase_plant_1 = models.CharField(
        max_length=100, blank=True, null=True
    )
    phenological_phase_plant_2 = models.CharField(
        max_length=100, blank=True, null=True
    )
    phenological_phase_plant_3 = models.CharField(
        max_length=100, blank=True, null=True
    )
    phenological_phase_plant_4 = models.CharField(
        max_length=100, blank=True, null=True
    )
    phenological_phase_plant_5 = models.CharField(
        max_length=100, blank=True, null=True
    )
    phenological_phase_plant_6 = models.CharField(
        max_length=100, blank=True, null=True
    )
    phenological_phase_plant_7 = models.CharField(
        max_length=100, blank=True, null=True
    )
    phenological_phase_plant_8 = models.CharField(
        max_length=100, blank=True, null=True
    )
    phenological_phase_plant_9 = models.CharField(
        max_length=100, blank=True, null=True
    )
    phenological_phase_plant_10 = models.CharField(
        max_length=100, blank=True, null=True
    )

    # Custom notes field for additional observations
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Agro3 Report for {self.crop} in {self.district}, {self.year}"
