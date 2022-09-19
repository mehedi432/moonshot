from django.contrib import admin
from .models import Post

from modeltranslation.admin import TabbedTranslationAdmin,TranslationAdmin

# Install and activate summernote
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.utils import get_attachment_model
admin.site.unregister(get_attachment_model())


# creating admin class
class BlogAdmin(SummernoteModelAdmin,TranslationAdmin):
    exclude = ('time', 'slug',)
    prepopulated_fields = {"slug": ["title",]}
    # displaying posts with title slug and created time
    list_display = ('title', 'slug', 'create_at', 'status')
    # list_filter = ("status", )
    search_fields = ['title', 'content']
    summernote_fields = ('content', )
    group_fieldsets = True

# registering admin class
admin.site.register(Post, BlogAdmin)
