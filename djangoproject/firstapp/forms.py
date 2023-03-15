from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    emailid = forms.EmailField()
    file = forms.ImageField()
