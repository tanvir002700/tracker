from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordResetView

urlpatterns = [
    url(r'^detail/$', views.AccountDetailView.as_view(), name='detail'),
    url(r'^registration/$', views.RegistrationView.as_view(), name='registration'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^password_reset/$', views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'password_reset/complete', views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]

