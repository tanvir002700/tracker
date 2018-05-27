from django.forms import ModelForm
from django import forms
from .models import Leave


class LeaveForm(ModelForm):
    leave_reason = forms.CharField(required=True, widget=forms.Textarea)
    date_from = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
    date_to = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))

    class Meta:
        model = Leave
        fields = ['leave_type', 'leave_reason', 'date_from', 'date_to']
