from modeltranslation.translator import translator, TranslationOptions
from product.models import *


class ProductTranslationOptions(TranslationOptions):
    fields = ('name',)


class ProductVariantTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'characteristics')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class CharacteristicsTranslationOptions(TranslationOptions):
    fields = ('key',)


class CharacteristicsValueTranslationOptions(TranslationOptions):
    fields = ('value',)


class AttributeTranslationOptions(TranslationOptions):
    fields = ('name',)


class AttributeValueTranslationOptions(TranslationOptions):
    fields = ('value',)


translator.register(Product, ProductTranslationOptions)
translator.register(ProductVariant, ProductVariantTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Attribute, AttributeTranslationOptions)
translator.register(AttributeValue, AttributeValueTranslationOptions)
