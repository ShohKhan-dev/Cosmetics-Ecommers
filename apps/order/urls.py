# Django
from django.urls import path

# Project
from .views.admin_update import AdminUpdateOrderStatusView
from .views.create_update import (
    AddOrderProductAPIView, UpdateOrderProductAPIView,
    DeleteOrderProductAPIView, AddListOrderProductAPIView
)
from .views.order_list import OrderListAPIView, OrderAdminListAPIView, OrderDetailAPIVIew
from .views.product_list import OrderProductListAPIVIew

urlpatterns = [
    path('list/', OrderListAPIView.as_view()),
    path('detail/<int:pk>/', OrderDetailAPIVIew.as_view()),
    path('admin/list/', OrderAdminListAPIView.as_view()),
    path('admin/update_status/', AdminUpdateOrderStatusView.as_view()),
    path('product/list/', OrderProductListAPIVIew.as_view()),
    path('product/add/', AddOrderProductAPIView.as_view()),
    path('product/add/list/', AddListOrderProductAPIView.as_view()),
    path('product/update/<int:pk>/', UpdateOrderProductAPIView.as_view()),
    path('product/delete/<int:pk>/', DeleteOrderProductAPIView.as_view()),
]
