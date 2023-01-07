from django.contrib import admin
from django.urls import path, include
from config import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include('user.urls')),
    path('api/v1/product/', include('product.urls')),
    path('api/v1/file/', include('file.urls')),
    path('api/v1/blog/', include('blog.urls')),
    path('api/v1/company_info/', include('company_info.urls')),
    path('api/v1/banner/', include('banners.urls')),
    path('api/v1/order/', include('order.urls')),
    path('api/v1/payment/', include('payment.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
