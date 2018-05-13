from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Leave

class LeaveViewCreateView(CreateView):
    model = Leave
    template_name = 'leave_tracker/leave_create_form.html'
