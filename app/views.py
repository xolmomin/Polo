from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from app.forms import RegisterForm


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
    template_name = 'app/login-page.html'


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


class FaqPage(TemplateView):
    template_name = 'app/faq.html'


class ComparePage(TemplateView):
    template_name = 'app/compare-page.html'


class AddressPage(TemplateView):
    template_name = 'app/addresses.html'


class ContactUsPage(TemplateView):
    template_name = 'app/contact-us.html'


class AboutUsPage(TemplateView):
    template_name = 'app/about_us.html'


class ForgotPasswordPage(TemplateView):
    template_name = 'app/forgot-password.html'
