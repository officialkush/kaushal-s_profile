from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Project


class StaticViewSitemap(Sitemap):

    priority = 0.8

    changefreq = "weekly"

    def items(self):
        return [
            "core:home",
            "core:about",
            "core:skills",
            "core:projects",
            "core:experience",
            "core:contact",
        ]

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):

    priority = 0.7

    changefreq = "monthly"

    def items(self):
        return Project.objects.all()

    def location(self, obj):
        return reverse("core:projects")