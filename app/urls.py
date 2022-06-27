from django.urls import path

from app.views import index, login_page

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_page, name='login_page'),
    path('register/', login_page, name='login_page'),
]
