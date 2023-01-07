from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views.attribute import *
from product.views.category import *
from product.views.discount import DiscountViewSet
from product.views.min_max_price import GetMinMaxPriceView
from product.views.product import *
from product.views.product import ProductVariantCheckView
from product.views.review import *
from product.views.product_favorite import *

router = DefaultRouter()
router.register('attribute', AttributeViewSet)
router.register('attribute_value', AttributeValueViewSet)
router.register('category', CategoryViewSet)
router.register('category_list', CategoryListViewSet)
router.register('product', ProductViewSet)
router.register('product_variant', ProductVariantViewSet)
router.register('discount', DiscountViewSet)
router.register('product_review', ProductReviewListViewSet)

urlpatterns = [
    path('product_variant_list/', ProductVariantListAPIView.as_view()),
    path('get_attribute_product/<int:pk>/', GetAttributeProductAPIView.as_view()),
    path('get_min_max_price/', GetMinMaxPriceView.as_view()),
    path('product_favorite/<int:pk>/', ProductFavoriteAPIView.as_view()),
    path('product_favorite/', ProductFavoriteListAPIView.as_view()),
    path('attribute_list/', AttributeFilterView.as_view()),
    path('product_variant_check/', ProductVariantCheckView.as_view()),
    path('', include(router.urls)),
]
