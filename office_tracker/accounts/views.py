from django.shortcuts import render
from django.views.generic import TemplateView

class AccountDetailView(TemplateView):
  template_name = 'account_detail.html'
