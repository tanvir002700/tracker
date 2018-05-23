from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Leave

class LeaveModifyMixin(object):
    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if (object.status != Leave.PENDING):
            messages.add_message(self.request, messages.WARNING, 'cant update', 'danger')
            return redirect(reverse_lazy('leave_tracker:leave_list'))
        messages.add_message(self.request, messages.INFO, 'successfully update')
        return super(LeaveModifyMixin, self).dispatch(request, *args, **kwargs)