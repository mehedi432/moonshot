from django.urls import path
from .views import BlogPageListView, BlogPageDetailView

urlpatterns = [
    path('blog/', BlogPageListView.as_view(), name='blog_home'),
    path('blog/<slug:slug>/', BlogPageDetailView.as_view(), name='blog_details')
]