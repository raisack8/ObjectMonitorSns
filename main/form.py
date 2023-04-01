from django import forms
from .consts import *

class CreateForm(forms.Form):
  title = forms.CharField(max_length=100)
  content = forms.CharField()
  category = forms.ChoiceField(
    choices=((item[0], item[1]) for item in ARTICLE_CATEGORY)
    )
  thumbnail = forms.ImageField()