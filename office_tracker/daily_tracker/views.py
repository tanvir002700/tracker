from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Attandance


class DailyLoginView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('daily_tracker:attandance_list')

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        if user.is_active_login() is False:
            attandance = Attandance(enter_at=timezone.now(), user=self.request.user)
            attandance.save()
            messages.add_message(self.request, messages.INFO, 'login succees')
        else:
            messages.add_message(self.request, messages.WARNING, 'already logged in', 'danger')
        return super(DailyLoginView, self).get_redirect_url(*args, **kwargs)


class DailyLogoutView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('daily_tracker:attandance_list')

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        if user.is_active_login() is True:
            attandance = user.attandance_set.last()
            attandance.logout()
            messages.add_message(self.request, messages.INFO, 'successfully logged out')
        else:
            messages.add_message(self.request, messages.INFO, 'There is no active login', 'danger')
        return super(DailyLogoutView, self).get_redirect_url(*args, **kwargs)



class AttandanceListView(LoginRequiredMixin, ListView):
    template_name = 'daily_tracker/attandance_list.html'
    model = Attandance
    paginate_by = 20
    ordering = ['enter_at']

    def get_queryset(self):
        self.queryset = self.request.user.attandance_set.all().reverse()
        return super(AttandanceListView, self).get_queryset()


class TodayAttandanceListView(LoginRequiredMixin, ListView):
    template_name = 'daily_tracker/today_attandance_list.html'
    model = Attandance
    paginate_by = 20
    ordering = ['enter_at']

    def get_queryset(self):
        self.queryset = Attandance.objects.filter(enter_at__gte=timezone.localtime(timezone.now()).date()).reverse()
        return super(TodayAttandanceListView, self).get_queryset()
