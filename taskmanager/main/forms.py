from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    sender = forms.EmailField(max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea, required=True)
