from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account, MyAccountManager

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = Account
        fields = ('username', 'email')