from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import PostListView, PostDetailView


urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path(
        "category/<int:category_id>/",
        PostListView.as_view(),
        name="post_list_by_category",
    ),
    path("post/<slug:slug>", PostDetailView.as_view(), name="post_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
