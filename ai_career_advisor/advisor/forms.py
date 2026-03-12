from django import forms
from .models import CareerAdvice

class CareerForm(forms.ModelForm):
    class Meta:
        model = CareerAdvice
        fields = ['skills']
        widgets = {
            'skills': forms.Textarea(
                attrs={
                    'placeholder': 'Enter your skills (Example: Python, SQL, HTML, CSS)',
                    'class': 'skill-box',
                    'rows': 4,
                    'cols': 40
                }
            )
        }
        labels = {
            'skills': 'Your Skills'
        }