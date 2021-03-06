from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from accounts.forms import RegistrationForm, AccountUpdateForm

class UserRegistrationView(FormView):
    template_name = 'accounts/registration.html'
    form_class = RegistrationForm

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        user = form.save()
        if user:
            return redirect(reverse_lazy('accounts:detail'))

        return render(request, self.template_name, {'form': form})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/update.html'
    form_class = AccountUpdateForm

    def get_success_url(self):
        return reverse_lazy('accounts:detail')

    def get_object(self, queryset=None):
        return self.request.user


class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/detail.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user
