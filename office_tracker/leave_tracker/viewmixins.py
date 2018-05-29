from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Leave

class LeaveModifyMixin(object):
    success_message = ''
    failed_message = ''
    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.status != Leave.PENDING:
            messages.add_message(self.request, messages.WARNING, self.failed_message, 'danger')
            return redirect(reverse_lazy('leave_tracker:leave_list'))
        messages.add_message(self.request, messages.INFO, self.success_message)
        return super(LeaveModifyMixin, self).post(request, *args, **kwargs)
