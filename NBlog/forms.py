from django import forms
from NBlog.models import Comment, Bloger
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('This email address is already in use')
        return email


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError('This email address is already in use')
        return email


class BlogerUpdateForm(forms.ModelForm):
    class Meta:
        model = Bloger
        fields = ['date_of_birth', 'genre', 'bloger_bio', 'image']
        widgets = {'date_of_birth': forms.DateInput(attrs={
            'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
            'class': 'form-control'
        })}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
