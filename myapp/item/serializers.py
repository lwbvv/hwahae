from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('__all__')

class IngreScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('oily', 'dry', 'sensitive', )

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('ingredients',)


class ManySerializer(serializers.ModelSerializer):
    connect_ingre = IngredientSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('id','name','connect_ingre',)









class ProductInSerializer(serializers.ModelSerializer):
    connect_ingre = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all(), many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'connect_ingre')







class ProSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)

    class Meta:
        model = Product
        fields = ('product',)

class InSerializer(serializers.ModelSerializer):
    ingre_list = ManySerializer(many=True, read_only=True)

    class Meta:
        model = Ingredient
        fields = ('__all__')
