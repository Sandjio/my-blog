from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = context["posts"]

        for post in posts:
            paragraphs = post.content.split("\n")
            post.preview_content = "\n\n".join(paragraphs[:5])
            post.has_more_content = len(paragraphs) > 5

        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"
