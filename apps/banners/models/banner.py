from django.db import models

from core.base_model import BaseModel


class Banner(BaseModel):
    HOME = 'home'
    BRAND = 'brand'
    ABOUT = 'about'
    FAQ = 'faq'
    CONTACT = 'contact'
    PRODUCT = 'product'
    TAGS = (
        (HOME, 'home'),
        (BRAND, 'brand'),
        (ABOUT, 'about'),
        (FAQ, 'faq'),
        (CONTACT, 'contact'),
        (PRODUCT, 'product')
    )

    EN = 'en'
    RU = 'ru'
    DE = 'de'
    LANGUAGES = (
        (EN, EN),
        (RU, RU),
        (DE, DE)
    )
    title = models.CharField(max_length=63)
    description = models.CharField(max_length=155)
    image = models.ForeignKey('file.File', on_delete=models.CASCADE, related_name='banners')
    is_active = models.BooleanField(default=False)
    language = models.CharField(max_length=2, choices=LANGUAGES, default=EN)
    tag = models.CharField(max_length=15, choices=TAGS, default=HOME)

    def __str__(self) -> str:
        return self.title
