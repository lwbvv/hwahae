from rest_framework import serializers
# import os
# import sys
# sys.path.append('/home/ubuntu/lee/django-template-master/myapp')
from myapp.item.models import *


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'imageUrl', 'name', 'price', 'ingredients', 'monthlySales',)

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('oilyScore', 'dryScore', 'sensitiveScore', 'connect_ingre',)

class ProductRecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'imageUrl', 'name', 'price',)
