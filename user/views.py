from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView, LogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic import CreateView, FormView, TemplateView
from .forms import CustomUserCreationForm
from .models import CustomUser


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('user:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save(commit=True)

        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')

        return response


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('catalog:home')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserPasswordResetView(FormView):
    template_name = 'registration/password_form.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('user:password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        new_password = get_random_string(length=12)

        user = CustomUser.objects.get(email=email)
        user.set_password(new_password)
        user.save()

        send_mail(
            subject='Password Reset Request',
            message=f'Your new password is: {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )

        return super().form_valid(form)


class UserPasswordResetDoneView(PasswordResetDoneView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/send_password.html'
    success_url = reverse_lazy('user:password_reset_done')


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/confirm_password.html'
    success_url = reverse_lazy('password_reset_confirm')


class UserPasswordResetCompleteView(PasswordResetCompleteView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_reset_done')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
