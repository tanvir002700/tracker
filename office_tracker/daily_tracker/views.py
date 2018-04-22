from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from .models import Attandance


class DailyLoginView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('accounts:detail')

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        if user.is_active_login() == False:
            attandance = Attandance(enter_at=timezone.now(), user=self.request.user)
            attandance.save()
        return super(DailyLoginView, self).get_redirect_url(*args, **kwargs)

