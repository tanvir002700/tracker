from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Leave
from .forms import LeaveForm

class LeaveCreateView(CreateView):
    model = Leave
    template_name = 'leave_tracker/leave_create_form.html'
    form_class = LeaveForm


class LeaveListView(ListView):
    model = Leave
    template_name = 'leave_tracker/leave_list.html'
