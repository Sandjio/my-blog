from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.views.generic import ListView, DetailView
from .models import Post, Category


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]
    paginate_by = 5

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        if category_id:
            category = get_object_or_404(Category, id=category_id)
            return Post.objects.filter(categories=category, is_published=True)
        return Post.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = context["posts"]
        context["categories"] = Category.objects.all().annotate(
            post_count=Count("posts")
        )

        for post in posts:
            paragraphs = post.content.split("\n")
            post.preview_content = "\n\n".join(paragraphs[:5])
            post.has_more_content = len(paragraphs) > 5

        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"
