from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # /auth/login
    path("",include("apps.apitest.urls")),
    path('auth/', include("apps.jcauth.urls")),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)