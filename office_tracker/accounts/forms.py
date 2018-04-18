from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        if not self.is_valid():
            return None
        user = super(RegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class AccountUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

