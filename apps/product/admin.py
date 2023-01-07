from django.contrib import admin
from product.models import *

# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(ProductFavorite)
admin.site.register(AttributeValue)
admin.site.register(Attribute)
admin.site.register(Discount)
