from django.urls import path

from app.views import IndexPage, LoginPage, LogoutPage, ProductPage, ProductDetailPage, QuickViewPage, AllProductPage, \
    RegisterPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('login/', LoginPage.as_view(), name='login_page'),
    path('register/', RegisterPage.as_view(), name='register_page'),
    path('logout/', LogoutPage.as_view(), name='logout_page'),
    path('product-list/', ProductPage.as_view(), name='product_list'),
    path('all-product-list/', AllProductPage.as_view(), name='all_product_list'),
    path('product-detail/', ProductDetailPage.as_view(), name='product_detail'),
    path('quick-view-product/', QuickViewPage.as_view(), name='quick_view_product'),
]
