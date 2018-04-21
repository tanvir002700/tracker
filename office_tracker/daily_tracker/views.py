from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin


class DailyLoginView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('accounts:detail')

    def get_redirect_url(self, *args, **kwargs):
        print("come here")
        return super(DailyLoginView, self).get_redirect_url(*args, **kwargs)

