from django import forms
from .models.agro1_form import Agro1

class Agro1Form(forms.ModelForm):
    class Meta:
        model = Agro1
        fields = [
            'country', 'district', 'station', 'field', 'crop', 'variety', 'date_of_sowing', 
            'observer_name', 'date_of_observation', 'phenological_phase', 'number_of_plants_with_features',
            'percentage_of_plants_with_features', 'replication_1', 'replication_2', 'replication_3',
            'replication_4', 'total_replication', 'field_work_1', 'field_work_2', 'field_work_3',
            'field_work_4', 'notes'
        ]
        
    # Optional: Custom validation or field handling
    def clean_date_of_observation(self):
        date_of_observation = self.cleaned_data.get('date_of_observation')
        if date_of_observation > self.instance.date_of_sowing:
            raise forms.ValidationError("Date of observation must be after the date of sowing.")
        return date_of_observation

    def clean_percentage_of_plants_with_features(self):
        percentage = self.cleaned_data.get('percentage_of_plants_with_features')
        if not (0 <= percentage <= 100):
            raise forms.ValidationError("Percentage must be between 0 and 100.")
        return percentage
