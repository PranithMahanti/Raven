from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name'}), max_length=200)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your Email'}), max_length=200)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}), max_length=200)
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}))
