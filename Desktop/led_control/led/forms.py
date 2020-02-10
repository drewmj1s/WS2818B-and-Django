from django import forms
from .models import Pattern

class PatternForm(forms.ModelForm):
    class Meta:
        model = Pattern
        fields = ['name', 'back_and_forth', 'colors', 'num_leds', 'speed_var']
        widths = {
            'name' : forms.TextInput(
                attrs = { 'class': 'form-control', 'placeholder': 'Enter pattern name', 'aria-label' : 'Pattern', 'aria-describedby': 'add-btn'}),
            'colors' : forms.TextInput(
                attrs= {'class': 'form-control', 'placeholder': 'Enter color value', 'aria-label' : 'Pattern', 'aria-describedby': 'add-btn'}),
            'num_leds' : forms.IntegerField(),
            'speed_var' : forms.IntegerField(),
            'back_and_forth' : forms.BooleanField(),
            
        }