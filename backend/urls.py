from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),

    path('accounts/', include('allauth.urls')),
    path('api/v1/', include('apps.core.api.urls')),
    path('api-auth/', include('rest_framework.urls')),

    re_path('.*', TemplateView.as_view(template_name='index.html')),
]
