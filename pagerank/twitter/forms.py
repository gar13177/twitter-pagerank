from django import forms

class TwitterForm(forms.Form):
    subject = forms.CharField(max_length=100)