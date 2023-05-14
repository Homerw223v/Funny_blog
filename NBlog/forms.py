from django import forms
from NBlog.models import Comment, Bloger
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.conf import settings
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

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
        fields = ['genre', 'bloger_bio', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
