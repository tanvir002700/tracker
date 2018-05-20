from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Leave
from .forms import LeaveForm


class LeaveListView(LoginRequiredMixin, ListView):
    model = Leave
    template_name = 'leave_tracker/leave_list.html'


class LeaveDetailView(LoginRequiredMixin, DetailView):
    model = Leave
    template_name = 'leave_tracker/leave_detail.html'
    context_object_name = 'leave'


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
    success_message = 'successfully saved!!!!'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if (object.status != Leave.PENDING):
            messages.add_message(self.request, messages.WARNING, 'cant update', 'danger')
            return redirect(reverse_lazy('leave_tracker:leave_list'))
        messages.add_message(self.request, messages.INFO, 'successfully update')
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)



class LeaveDeleteView(LoginRequiredMixin, DeleteView):
    model = Leave
    template_name = 'leave_tracker/leave_confirm_delete.html'
    success_url = reverse_lazy('leave_tracker:leave_list')

