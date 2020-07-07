from django.contrib import admin
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),

    path('accounts/', include('allauth.urls')),
    path('api/v1/', include('apps.core.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
