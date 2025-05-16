from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    author = models.CharField(max_length=200)
    public =models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    post_image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title