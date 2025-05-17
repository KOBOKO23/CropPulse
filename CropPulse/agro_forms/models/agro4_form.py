from django.db import models
from .base import BaseAgroModel


class Agro4(BaseAgroModel):
    # Kind of Observation
    agro_crop = models.CharField(max_length=100)  # Specific crop type
    
    # Phenological Phase
    phenological_phase = models.CharField(max_length=100) 

    # General Assessment of the State (marks)
    state_assessment = models.IntegerField()  # assessment in marks (e.g.,1-10)

    # Sowing Density
    sowing_density_plants = models.IntegerField()  # No. of plants per hectare.
    sowing_density_stems = models.IntegerField()  # No. of stems per m²

    # Plant Height
    plant_height = models.IntegerField()  # Height in cm
   
    # Damage from Meteorological Phenomena
    met_phenomena_name = models.CharField(max_length=100)  # Name of met phenomena
    met_phenomena_date = models.DateField()  # Date of the event
    met_phenomena_duration = models.CharField(max_length=100)  # Duration of the phenomena
    met_phenomena_damage_type = models.CharField(max_length=100)  # Type of damage caused
    met_phenomena_damage_extent = models.IntegerField()  # Extent of the damage in percentage
    
    # Damage from Pests and Diseases
    pests_or_diseases_name = models.CharField(max_length=100)  # Name of pests or diseases
    pests_or_diseases_date = models.DateField()  # Date of the damage
    pests_or_diseases_damage_type = models.CharField(max_length=100)  # Type of damage caused
    pests_or_diseases_damage_extent = models.IntegerField()  # Extent of the damage in percentage
    
    # Extent of the Spreading of Weeds
    weeds_spread_extent = models.IntegerField()  # Weeds spread extent in marks (e.g., 1-10)
    
    # Yield of the Crop
    crop_yield = models.CharField(max_length=100)  # Yield (e.g., kg/ha, tons, etc.)
    harvesting_date = models.DateField()  # Date of harvesting
    
    def __str__(self):
        return f"Agro4 Report for {self.crop} in {self.district}, {self.year}"
