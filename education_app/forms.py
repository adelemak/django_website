from django import forms
from .models import StudentProfile


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = '__all__'
        widgets = {
            'course': forms.Select(),
            'gpa': forms.NumberInput(attrs={'step': 0.1, 'min': 0}),
        }