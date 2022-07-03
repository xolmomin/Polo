from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from root import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('accounts/', include('allauth.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

