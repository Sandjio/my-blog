from django.views.generic import ListView, DetailView, TemplateView
from .models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = "posts"
    ordering = ["-created_at"]
    paginate_by = 5


# class PostDetailView(DetailView):
#     model = Post
#     template_name = "post_detail.html"
#     context_object_name = "post"
#     ordering = ["-created_at"]
#     paginate_by = 5


class PostDetailView(TemplateView):
    template_name = "post_detail.html"
