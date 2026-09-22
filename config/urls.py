from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("notification.urls")),
    path("api/doc/", SpectacularAPIView.as_view(), name="docs"),
    path("api/swagger/", SpectacularSwaggerView.as_view(url_name="docs"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="docs"), name="redoc-ui")
]
