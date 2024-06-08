from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("shop/", include("shop.urls")),
    path("accounts/", include("allauth.urls")),
    path("", RedirectView.as_view(url="shop/", permanent=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "shop.views.error_404_view"
