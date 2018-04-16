from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse, reverse_lazy
from .forms import RegistrationForm


class RegistrationView(FormView):
    template_name = 'accounts/registration.html'
    form_class = RegistrationForm

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        user = form.save()
        if user:
            return redirect(reverse('accounts:detail'))
        else:
            return render(request, self.template_name, {'form': form})


class LoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse('accounts:detail')

class LogoutView(LogoutView):
    template_name = 'accounts/logout.html'

    def get_next_page(self):
        return reverse('accounts:login')


class AccountDetailView(TemplateView):
    template_name = 'accounts/account_detail.html'


class PasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_done')


class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/passowrd_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')



class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'
