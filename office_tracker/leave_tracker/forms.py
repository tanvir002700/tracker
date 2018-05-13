from django.forms import ModelForm
from .models import Leave
from django import forms


class LeaveForm(ModelForm):
    leave_reason = forms.CharField(required=True, widget=forms.Textarea)

    class Meta:
        model = Leave
        fields = ['leave_type', 'leave_reason']
