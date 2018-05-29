from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Leave

class LeaveModifyMixin(object):
    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.status != Leave.PENDING:
            messages.add_message(self.request, messages.WARNING, 'cant update', 'danger')
            return redirect(reverse_lazy('leave_tracker:leave_list'))
        print("come here....................")
        messages.add_message(self.request, messages.INFO, 'successfully update')
        print(type(messages))
        return super(LeaveModifyMixin, self).post(request, *args, **kwargs)
