from django.shortcuts import render
from django.views.generic import ListView , DetailView 
from django.views.generic.edit import  CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class TopicView (ListView):
    model = Post
    template_name = "home.html"

class TopicDetailView (DetailView):
    model = Post
    template_name = "post_detail.html"

class TopicCreateView (CreateView):
    model = Post
    template_name = "post_new.html"
    fields = "__all__"

class TopicUpdateView (UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title","body"]

class TopicDeleteView (DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
    