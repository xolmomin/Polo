from django.urls import path

from app.views import IndexPage, LoginPage, LogoutPage, ProductPage, ProductDetailPage, QuickViewPage, AllProductPage, \
    RegisterPage, FaqPage, ComparePage, AddressPage, ContactUsPage, AboutUsPage, ForgotPasswordPage, MyWishesPage, \
    DashboardPage, ShoppingCardsPage, CheckOutPage, BlogPage, ProductList, BlogDetailsPage, Product_Detail_Page

urlpatterns = [
    # main url
    path('', IndexPage, name='index'),

    # auth urls
    path('login/', LoginPage.as_view(), name='login_page'),
    path('register/', RegisterPage.as_view(), name='register_page'),
    path('logout/', LogoutPage.as_view(), name='logout_page'),
    path('forgot-password/', ForgotPasswordPage.as_view(), name='forgot_password_page'),

    # products url
    path('product-list/', ProductPage.as_view(), name='product_list'),
    path('all-product-list/', AllProductPage.as_view(), name='all_product_list'),
    path('product-detail/', ProductDetailPage.as_view(), name='product_detail'),
    path('product-detail/<int:product_id>', Product_Detail_Page, name='product_detail_with_id'),
    path('compare/', ComparePage.as_view(), name='compare_page'),
    path('dashboard/', DashboardPage.as_view(), name='dashboard_page'),
    path('quick-view-product/', QuickViewPage.as_view(), name='quick_view_product'),
    path('list-product/', ProductList.as_view(), name='list_product'),

    # about company urls
    path('faq-page/', FaqPage.as_view(), name='faq_page'),
    path('address/', AddressPage.as_view(), name='address_page'),
    path('contact-us/', ContactUsPage.as_view(), name='contact-us-page'),
    path('about-us/', AboutUsPage.as_view(), name='about-us-page'),

    # blog
    path('polo-blog/', BlogPage.as_view(), name='blog_page'),
    path('blog-details/', BlogDetailsPage.as_view(), name='blog_details_page'),

    # user urls
    path('my-wishes/', MyWishesPage.as_view(), name='my_wishlist_page'),
    path('shopping-cards/', ShoppingCardsPage.as_view(), name='shopping_cards_page'),
    path('check-out/', CheckOutPage.as_view(), name='check_out_page'),
]
