from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView
from app.forms import RegisterForm


class RegisterPage(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('login_page')
    template_name = 'app/register.html'

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            level=messages.WARNING,
            message='You are successfully registered '
        )
        return super().form_valid(form)


class LogoutPage(LogoutView):
    template_name = 'app/logout.html'


def index(request):
    return render(request, 'app/index.html')\

def login(request):
    return render(request , 'app/login.html')
def register(request):
    return render(request , 'app/register-page.html')
