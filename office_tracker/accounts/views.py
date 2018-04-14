from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
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


class AccountDetailView(TemplateView):
  template_name = 'accounts/account_detail.html'
