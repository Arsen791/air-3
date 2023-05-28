from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('order', views.order),
    path('create', views.create),
    path('crship', views.crship),
    path('shiplist', views.shiplist, name='shiplist'),
    path('orders/delete/<int:pk>/', views.delete_order_detail, name='delete_my_model'),
    path('orders/change/<int:pk>/', views.change_order_detail)
]
