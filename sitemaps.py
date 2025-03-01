from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from Posts.models import Post


class BlogSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse("post_detail", args=[obj.slug])
