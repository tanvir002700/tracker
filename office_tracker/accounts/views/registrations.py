from django.views.generic.edit import FormView
from accounts.forms import RegistrationForm
from django.views.generic.edit import UpdateView
from accounts.forms import RegistrationForm, AccountUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

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


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'accounts/update.html'
    form_class = AccountUpdateForm

    def get_success_url(self):
        return reverse('accounts:detail')

    def get_object(self, queryset=None):
        return self.request.user


class AccountDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/detail.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

