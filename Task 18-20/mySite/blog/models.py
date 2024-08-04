from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    signature = models.CharField(max_length=140, default="Developers are not born, they're made.")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
