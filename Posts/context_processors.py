from django.db.models import Count
from .models import Category, Post


def categories_processor(request):
    categories = Category.objects.all().annotate(post_count=Count("posts"))
    return {"categories": categories}


def posts_processor(request):
    posts = Post.objects.all()
    return {"posts": posts}
