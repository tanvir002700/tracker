from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^detail/$', views.AccountDetailView.as_view(), name='detail')
]

