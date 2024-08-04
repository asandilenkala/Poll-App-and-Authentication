from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    # The title of the blog post, limited to 200 characters
    title = models.CharField(max_length=200)
    
    # The main content of the blog post
    body = models.TextField()
    
    # A short signature or tagline for the post, with a default value
    signature = models.CharField(max_length=140, default="Developers are not born, they're made.")
    
    # The date and time when the post was created, automatically set on creation
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # String representation of the Post object, returning the title
        return self.title
