from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('test', views.test),
    path('order', views.order),
    path('create', views.create),
    path('crship', views.crship),
    path('shiplist', views.shiplist, name='shiplist'),
    path('orders/delete/<int:pk>/', views.delete_order_detail, name='delete_my_model'),
    path('orders/change/<int:pk>/', views.change_order_detail),
    path('order/<int:pk>/', views.edit_detail, name='edit_detail'),
    path('get_last_order_name/', views.get_last_order_name, name='get_last_order_name'),

    
]
