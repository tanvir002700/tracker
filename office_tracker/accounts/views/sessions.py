from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

class UserLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'

    def get_success_url(self):
        return reverse_lazy('root')


class UserLogoutView(LogoutView):
    template_name = 'accounts/logout.html'

    def get_next_page(self):
        return reverse_lazy('accounts:login')
