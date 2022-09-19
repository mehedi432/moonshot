from django.views.generic import ListView, DetailView
from .models import Post


class BlogPageListView(ListView):
    model = Post
    context_object_name = 'post_list'
    queryset = Post.objects.filter(status='published')


class BlogPageDetailView(DetailView):
    model = Post