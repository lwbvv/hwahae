from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

# router = DefaultRouter()
# router.register('user', views.UserCreate)



urlpatterns = [
    path('product', views.Products.as_view(), name='product'),
    path('ingredients', views.Ingredients.as_view(), name='ingredients'),
    path('score', views.Score.as_view(), name='score'),
    # path('many', views.SaveTables.as_view(), name='many'),
    # path('inter', views.Intermediary.as_view(), name='many'),
]
