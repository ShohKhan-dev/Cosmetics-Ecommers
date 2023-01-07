from modeltranslation.translator import translator, TranslationOptions

from banners.models import *


class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Banner, BannerTranslationOptions)
