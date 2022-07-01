from django.contrib import messages
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from app.forms import RegisterForm, LoginForm


class RegisterPage(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('login_page')
    template_name = 'app/register-page.html'

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            level=messages.WARNING,
            message='You are successfully registered '
        )
        return super().form_valid(form)


class LogoutPage(LogoutView):
    template_name = 'app/logout-page.html'


class LoginPage(LoginView):
    form_class = LoginForm
    template_name = 'app/login-page.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class IndexPage(TemplateView):
    template_name = 'app/index.html'


class ProductPage(TemplateView):
    template_name = 'app/product-list.html'


class AllProductPage(TemplateView):
    template_name = 'app/all-product-list.html'


class ProductDetailPage(TemplateView):
    template_name = 'app/product-detail-page.html'

class QuickViewPage(TemplateView):
    template_name = 'app/quick-view-page.html'

