from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "Storefront Admin"
admin.site.index_title = "Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("app/", include("playground.urls")),
    path("store/", include("store.urls")),
] + debug_toolbar_urls()
