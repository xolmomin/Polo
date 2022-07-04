from django.contrib import messages
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from app.forms import RegisterForm
from app.models import Product, Category

from app.forms import RegisterForm, LoginForm
from app.models import Product


class RegisterPage(FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('login_page')
    template_name = 'app/main/register-page.html'

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
    template_name = 'app/main/login-page.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        return super().form_valid(form)


class IndexPage(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Products'] = Product.objects.all()
        context['Categorys'] = Category.objects.all()

        return context


class ProductPage(TemplateView):
    template_name = 'app/products/product-list.html'


class AllProductPage(TemplateView):
    template_name = 'app/products/all-product-list.html'


class ProductDetailPage(TemplateView):
    template_name = 'app/products/product-detail-page.html'


class Product_Detail_Page(TemplateView):
    template_name = 'app/products/product-detail-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.filter(id=kwargs.get('product_id')).first()
        context['price'] = int(product.price)
        context['discount'] = int(product.price) - (int(product.price) * (product.discount / 100))
        context['product'] = product

        # auth
        all_category = Category.objects.filter(level=2)
        all_products = Product.objects.all()
        context['all_category'] = all_category
        context['all_products'] = all_products

        return context


class QuickViewPage(TemplateView):
    template_name = 'app/company/quick-view-page.html'


class FaqPage(TemplateView):
    template_name = 'app/company/faq.html'


class ComparePage(TemplateView):
    template_name = 'app/products/compare-page.html'


class AddressPage(TemplateView):
    template_name = 'app/company/addresses.html'


class ContactUsPage(TemplateView):
    template_name = 'app/company/contact-us.html'


class AboutUsPage(TemplateView):
    template_name = 'app/company/about_us.html'


class ForgotPasswordPage(TemplateView):
    template_name = 'app/main/forgot-password.html'


class MyWishesPage(TemplateView):
    template_name = 'app/products/my-wishlist-page.html'


class CheckOutPage(TemplateView):
    template_name = 'app/products/checkout-page.html'


class DashboardPage(TemplateView):
    template_name = 'app/products/dashboard-page.html'


class ShoppingCardsPage(TemplateView):
    template_name = 'app/products/shopping-cart-page.html'


class BlogPage(TemplateView):
    template_name = 'app/company/blog.html'


class BlogDetailsPage(TemplateView):
    template_name = 'app/company/blog_detail.html'


class ProductList(TemplateView):
    template_name = 'app/products/list.html'
