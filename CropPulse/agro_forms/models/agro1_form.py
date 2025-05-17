# agro1_form.py
from django.db import models
from .base import BaseAgroModel


class Agro1(BaseAgroModel):
    # Phenological Observation fields
    date_of_observation = models.DateField()
    phenological_phase = models.CharField(max_length=100)
    number_of_plants_with_features = models.IntegerField()
    percentage_of_plants_with_features = models.IntegerField()

    # Replication fields (for each replication)
    replication_1 = models.IntegerField()
    replication_2 = models.IntegerField()
    replication_3 = models.IntegerField()
    replication_4 = models.IntegerField()
    total_replication = models.IntegerField()

    # Field Work notes
    field_work_1 = models.TextField()
    field_work_2 = models.TextField()
    field_work_3 = models.TextField()
    field_work_4 = models.TextField()

    # Custom notes field
    notes = models.TextField()  # Custom field specific to Agro1

    def __str__(self):
        return f"Agro1 Report for {self.crop} in {self.district}, {self.year}"
