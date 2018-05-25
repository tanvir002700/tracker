# pylint: disable=invalid-name
from django.urls import path, re_path
from .views.registrations import UserRegistrationView, UserUpdateView, UserDetailView
from .views.sessions import UserLoginView, UserLogoutView
from .views.passwords import UserPasswordResetView, UserPasswordResetDoneView, UserPasswordResetConfirmView,\
                             UserPasswordResetCompleteView

urlpatterns = [
    path('detail/', UserDetailView.as_view(), name='detail'),
    path('update/', UserUpdateView.as_view(), name='update'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
            UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete')
]
