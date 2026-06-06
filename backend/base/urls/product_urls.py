from django.urls import path
from base.views import product_views as views

urlpatterns = [
    path('', views.getProducts, name='products'),
    
    path('create/', views.createProduct, name='product-create'),
    path('upload-image/', views.uploadImage, name='product-upload-image'),

    path('<str:id>/review/', views.createProductReview, name='product-review'),
    path('top/', views.getTopProducts, name='product-top'),
    path('<str:id>/', views.getProduct, name='product'),
    
    path('update/<str:id>/', views.updateProduct, name='product-update'),
    path('delete/<str:id>/', views.deleteProduct, name='product-delete'),
]
