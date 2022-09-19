import readtime
from django.db import models
from django.urls import reverse


class Post(models.Model):
    PUBLISH_STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=233, unique=True)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    status = models.CharField(max_length=89, choices=PUBLISH_STATUS, default='draft')
    time = models.CharField(max_length=233,)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def get_readtime(self):
        result = readtime.of_text(self.content)
        return result.text
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_details", kwargs={"slug": self.slug})
    
    