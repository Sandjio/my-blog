from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Category, Post, Tag


# Create your tests here.
class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="Django", description="Django category"
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Django")
        self.assertEqual(self.category.description, "Django category")

    def test_category_str(self):
        self.assertEqual(str(self.category), "Django")


class PostModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="12345"
        )
        self.category = Category.objects.create(
            name="Django", description="Django category"
        )
        self.tag = Tag.objects.create(name="Python")
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.user,
            slug="test-post",
            is_published=True,
        )
        self.post.categories.add(self.category)
        self.post.tags.add(self.tag)

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "This is a test post.")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.slug, "test-post")
        self.assertTrue(self.post.is_published)

    def test_post_str(self):
        self.assertEqual(str(self.post), "Test Post")

    def test_get_absolute_url(self):
        self.assertEqual(
            self.post.get_absolute_url(),
            reverse("post_detail", kwargs={"slug": "test-post"}),
        )

    def test_post_category_relationship(self):
        self.assertIn(self.category, self.post.categories.all())

    def test_post_tag_relationship(self):
        self.assertIn(self.tag, self.post.tags.all())


class PostListViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="12345"
        )
        self.category = Category.objects.create(
            name="Django", description="Django category"
        )
        self.tag = Tag.objects.create(name="Python")
        for i in range(10):
            post = Post.objects.create(
                title=f"Test Post {i}",
                content="This is a test post.",
                author=self.user,
                slug=f"test-post-{i}",
                image="image.jpg",
                is_published=True,
            )
            post.categories.add(self.category)
            post.tags.add(self.tag)

    def test_post_list_view(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_list.html")
        self.assertEqual(len(response.context["posts"]), 5)  # paginate_by is 5

    def test_post_list_view_with_category(self):
        response = self.client.get(
            reverse("post_list_by_category", args=[self.category.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_list.html")
        self.assertEqual(len(response.context["posts"]), 5)  # paginate_by is 5
        for post in response.context["posts"]:
            self.assertIn(self.category, post.categories.all())

    def test_post_list_view_pagination(self):
        response = self.client.get(reverse("post_list") + "?page=2")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_list.html")
        self.assertEqual(len(response.context["posts"]), 5)  # paginate_by is 5


class PostDetailViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="12345"
        )
        self.category = Category.objects.create(
            name="Django", description="Django category"
        )
        self.tag = Tag.objects.create(name="Python")
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            author=self.user,
            slug="test-post",
            image="image.jpg",
            is_published=True,
        )
        self.post.categories.add(self.category)
        self.post.tags.add(self.tag)

    def test_post_detail_view(self):
        response = self.client.get(reverse("post_detail", args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_detail.html")
        self.assertEqual(response.context["post"], self.post)
