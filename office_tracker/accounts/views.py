from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import RegistrationForm


class RegistrationView(FormView):
  template_name = 'accounts/registration.html'
  form_class = RegistrationForm

  def post(self, request, *args, **kwargs):
    pass


class AccountDetailView(TemplateView):
  template_name = 'accounts/account_detail.html'
