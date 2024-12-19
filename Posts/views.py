from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"
    ordering = ["-created_at"]
    paginate_by = 5
