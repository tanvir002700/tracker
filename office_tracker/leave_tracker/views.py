from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .forms import LeaveForm
from .models import Leave
from .viewmixins import LeaveModifyMixin


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
    object = None
    user = None

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_season = self.user.userseason_set.last()
        return super(LeaveCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.user = request.user
        if self.user.userseason_set.count() == 0:
            messages.add_message(self.request, messages.WARNING, 'There is no user season', 'danger')
            return redirect(reverse_lazy('leave_tracker:leave_list'))
        return super(LeaveCreateView, self).post(request, *args, **kwargs)


class LeaveUpdateView(LoginRequiredMixin, LeaveModifyMixin, UpdateView):
    model = Leave
    template_name = 'leave_tracker/leave_form.html'
    form_class = LeaveForm
    success_url = reverse_lazy('leave_tracker:leave_list')
    success_message = 'successfully saved!!!!'
    failed_message = "can't saved!!!!"


class LeaveDeleteView(LoginRequiredMixin, LeaveModifyMixin, DeleteView):
    model = Leave
    template_name = 'leave_tracker/leave_confirm_delete.html'
    success_url = reverse_lazy('leave_tracker:leave_list')
    success_message = 'successfully Delete!!!!'
    failed_message = "can't Delete!!!!"
