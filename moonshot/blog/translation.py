from modeltranslation.translator import translator, TranslationOptions
from .models import Post

class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'time', 'status', 'create_at', 'content')

translator.register(Post, PostTranslationOptions)