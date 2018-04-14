from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^detail/$', views.AccountDetailView.as_view(), name='detail'),
  url(r'^registration/$', views.RegistrationView.as_view(), name='registration')
]

