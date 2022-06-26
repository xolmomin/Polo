from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import FormView, TemplateView

from app.forms import LoginForm, RegisterForm, ForgotPasswordForm, send_email
from app.models import User
from app.tokens import account_activation_token


class CreateUser(FormView):
    form_class = User
    success_url = None
    template_name = None


def index(request):
    return render(request, 'app/index.html')


def login_page(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
            return redirect('index')
        else:
            messages.add_message(
                request,
                level=messages.ERROR,
                message='Please enter correctly !'
            )
    return render(request, 'app/login.html', {'form': form})


class RegisterPage(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('login_page')
    template_name = 'app/register.html'

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            level=messages.WARNING,
            message='You are successfully create user'
        )
        return super().form_valid(form)


class LogoutPage(LogoutView):
    template_name = 'app/logout.html'


class ForgotPasswordPage(FormView):
    form_class = ForgotPasswordForm
    success_url = reverse_lazy('after_reset_page')
    template_name = 'app/forgot-password.html'

    def form_valid(self, form):
        send_email(form.data.get('email'), self.request, 'forgot')
        return super().form_valid(form)


class ActivateEmailView(TemplateView):
    template_name = 'app/comfirm-password.html'

    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uid')
        token = kwargs.get('token')

        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
        except Exception as e:
            print(e)
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            messages.add_message(
                request=request,
                level=messages.SUCCESS,
                message="Your account successfully activated!"
            )
            return redirect('index')
        else:
            return HttpResponse('Activation link is invalid!')
