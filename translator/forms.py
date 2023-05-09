from django import forms


class TranslatorForm(forms.Form):
    input = forms.CharField(widget=forms.TextInput)