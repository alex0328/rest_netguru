from django import forms
from netapp import models

class Movie_Post_Form(forms.Form):
    Title = forms.CharField(required=True)