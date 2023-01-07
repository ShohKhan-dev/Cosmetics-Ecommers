from modeltranslation.translator import translator, TranslationOptions
from blog.models import *


class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(Blog, BlogTranslationOptions)
