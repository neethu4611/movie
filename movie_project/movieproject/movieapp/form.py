from django import forms
from .models import Movies
class movie_form(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['name','desc','year','img']
