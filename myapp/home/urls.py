from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

# router = DefaultRouter()
# router.register('user', views.UserCreate)



urlpatterns = [
    path('products', views.Products.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetail.as_view(), name='productDetail'),
    # path('ingredients', views.Ingredients.as_view(), name='ingredients'),
]
