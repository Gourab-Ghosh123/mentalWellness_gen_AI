from django import forms
from .models import MoodSlider

class MoodSliderform(forms.ModelForm):
    
    class Meta:
        model = MoodSlider
        fields = ['mood_value']
        widgets = {
            'mood_value' : forms.NumberInput(
                attrs = { 'type' : 'range' , 'min' : '1' , 'max' : '10' , 'step' : '1' }
            )
        }