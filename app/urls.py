from django.urls import path

from app.views import index, login, register

urlpatterns = [
    path('', index, name='index'),
]
