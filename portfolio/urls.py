from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from core.sitemaps import StaticViewSitemap


sitemaps = {
    "static": StaticViewSitemap,
}


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "sitemap.xml",
        sitemap,
        {
            "sitemaps": sitemaps
        },
        name="django-sitemap",
    ),

    path(
        "dashboard/",
        include("dashboard.urls")
    ),

    path(
        "",
        include("core.urls")
    ),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )