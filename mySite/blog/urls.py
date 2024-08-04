from django.views.generic import ListView, DetailView
from django.urls import path
from .models import Post

# List of url paths.

urlpatterns = [
    # URL pattern for the blog homepage
    path('', 
        ListView.as_view(
            # Query to get the 25 most recent posts, ordered by date
            queryset=Post.objects.all().order_by("-date")[:25],
            # Template to use for rendering the list of posts
            template_name="blog.html"
        )
    ),
    # URL pattern for viewing the details of a specific post
    path('<int:pk>/',
        DetailView.as_view(
            # Model to use for retrieving the post details
            model=Post,
            # Template to use for rendering the post details
            template_name="post.html"
        )
    ),
]