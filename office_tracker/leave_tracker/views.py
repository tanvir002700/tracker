from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Leave
from .forms import LeaveForm


class LeaveListView(LoginRequiredMixin, ListView):
    model = Leave
    template_name = 'leave_tracker/leave_list.html'


class LeaveCreateView(LoginRequiredMixin, CreateView):
    model = Leave
    template_name = 'leave_tracker/leave_form.html'
    form_class = LeaveForm
    success_url = reverse_lazy('leave_tracker:leave_list')


class LeaveUpdateView(LoginRequiredMixin, UpdateView):
    model = Leave
    template_name = 'leave_tracker/leave_form.html'
    form_class = LeaveForm
    success_url = reverse_lazy('leave_tracker:leave_list')


class LeaveDeleteView(LoginRequiredMixin, DeleteView):
    model = Leave
    template_name = 'leave_tracker/leave_confirm_delete.html'
    success_url = reverse_lazy('leave_tracker:leave_list')

