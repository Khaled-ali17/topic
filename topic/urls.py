from django.urls import path
from .views import TopicView , TopicDetailView , TopicCreateView ,TopicUpdateView , TopicDeleteView

urlpatterns = [
    path("post/<int:pk>/delete/", TopicDeleteView.as_view(), name = "post_delete"),
    path("post/<int:pk>/edit/", TopicUpdateView.as_view(), name = "post_edit"),
    path("post/new/", TopicCreateView.as_view(), name = "post_new"),
    path("post/<int:pk>/", TopicDetailView.as_view(), name = "post_detail"),
    path("",TopicView.as_view(), name= "home"),
]