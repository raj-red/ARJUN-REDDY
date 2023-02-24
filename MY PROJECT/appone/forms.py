from django import forms
from appone.models import student


class STUDENTFORM(forms.ModelForm):
    class Meta:
        model = student
        fields ='__all__'
