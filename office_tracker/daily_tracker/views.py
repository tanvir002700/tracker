from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from .models import Attandance


class DailyLoginView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('daily_tracker:attandance_list')

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        if user.is_active_login() == False:
            attandance = Attandance(enter_at=timezone.now(), user=self.request.user)
            attandance.save()
        return super(DailyLoginView, self).get_redirect_url(*args, **kwargs)


class DailyLogoutView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('daily_tracker:attandance_list')

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        if user.is_active_login() == True:
            attandance = user.attandance_set.last()
            attandance.out_at = timezone.now()
            attandance.save()
        return super(DailyLogoutView, self).get_redirect_url(*args, **kwargs)



class AttandanceListView(ListView):
    template_name = 'daily_tracker/attandance_list.html'
    model = Attandance

    def get_queryset(self):
        self.queryset = self.request.user.attandance_set.all()
        return super(AttandanceListView, self).get_queryset()

