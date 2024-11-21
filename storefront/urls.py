from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Storefront Admin"
admin.site.index_title = "Admin"

urlpatterns = [
    path("", include("core.urls")),
    path("admin/", admin.site.urls),
    path("app/", include("playground.urls")),
    path("store/", include("store.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += [
        path("silk/", include("silk.urls", namespace="silk")),
    ]
