from django.test import TestCase , Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post
# Create your tests here.
class BoardTest (TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = "testuser", email = "test@gmail.com", password = "secret"
        )
        self.post = Post.objects.create(
            title = "a good title", body = "nice content" , author = self.user,
        )

    def test_string_representation (self):
        post = Post(title = "a simple title")
        self.assertEqual(str(post), post.title)

    def test_post_content (self):
        self.assertEqual(f"{self.post.title}", "a good title")
        self.assertEqual(f"{self.post.author}", "testuser")
        self.assertEqual(f"{self.post.body}", "nice content")

    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response , "nice content")
        self.assertTemplateUsed(response , "home.html")

    def test_post_detail_view(self):
        response = self.client.get("/post/1/")
        no_response = self.client.get("/post/1000/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response , "a good title")
        self.assertTemplateUsed(response , "post_detail.html")

    def test_post_create_view (self):
        response = self.client.post(
            reverse("post_new"),
            {"title": "new title" , "body": "new text" , "author": self.user},
        )
        self.assertEqual(response.status_code ,200)
        self.assertContains(response , "New title")
        self.assertContains(response , "New text")

    def test_post_update_view (self):
        response = self.client.post(
            reverse("edit post" , args="1"),
            {"title": "update title", "body": "update text",},
        )
        self.assertEqual(response.status_code,302)

    def test_post_delete_view(self):
        response = self.client.get(reverse("post_delete", args ="1"))
        self.assertEqual(response.status_code, 200)    






