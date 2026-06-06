from django.urls import path
from base.views import order_views as views

urlpatterns = [
    path('', views.listAllOrders, name='order-list-all'),
    
    path('listOrders/', views.listOrders, name='order-list'),
    path('add/', views.addOrderItems, name='order-add'),
    
    path('<str:id>/deliver/', views.updateOrderToDelivered, name='order-delivered'),  
    path('<str:id>/', views.getOrderById, name='order-detail'),
    path('<str:id>/pay/', views.updateOrderToPaid, name='order-pay'),
]
