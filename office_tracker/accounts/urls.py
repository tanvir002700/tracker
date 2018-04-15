from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^detail/$', views.AccountDetailView.as_view(), name='detail'),
    url(r'^registration/$', views.RegistrationView.as_view(), name='registration'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout')
]

