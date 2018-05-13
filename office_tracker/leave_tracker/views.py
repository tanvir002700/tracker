from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Leave

class CreateLeaveView(CreateView):
    model = Leave
    template_name = 'leave_tracker/create_leave_form.html'
