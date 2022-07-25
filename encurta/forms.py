from django import forms

class RegistroLink(forms.Form):
    url = forms.URLField()
