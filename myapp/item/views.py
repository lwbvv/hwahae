from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import permission_classes
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class Products(APIView):
    permission_classes = []

    #제품 리스트 db저장
    def post(self, request, format=None):
        for i in request.data:
            i['imageUrl'] = i.pop('imageId')
            serializer = ProductSerializer(data=i)
            if serializer.is_valid() :
                serializer.save()
        return Response("success", status=status.HTTP_201_CREATED)

class Ingredients(APIView):
    permission_classes = []
    # def get(self, request, format=None):
    #     image_name = Ingredient.objects.get(id =1)
    #     serializers = IngredientSerializer(image_name)
    #     return Response(serializers.data)

    #성분 리스트 db저장
    def post(self, request, format=None):

        for i in request.data:
            serializer = IngredientSerializer(data=i)
            if serializer.is_valid() :
                serializer.save()
        return Response("success", status=status.HTTP_201_CREATED)

class Score(APIView):

    #제품의 성분 스코어 계산하여 추가
    def post(self, request, format=None):
        product_obj = Product.objects.all() # 모든 제품의 데이터 가져오기
        score_serializers = ProductSerializer(product_obj, many = True) #성분 시리얼라이징
        count = 0
        for i in score_serializers.data: # 시리얼라이징한 데이터 순회
            ingre = i['ingredients']
            ingre_list = ingre.split(',')
            oily = 0
            sensitive = 0
            dry = 0
            for lists in ingre_list:
                ingre_odj = Ingredient.objects.get(name=lists)
                ingre_serializers = IngreScoreSerializer(ingre_odj)
                for key, value in ingre_serializers.data.items():
                    if key == 'oily':
                        if value == 'O':
                            oily += 1
                        elif value == 'X':
                            oily -= 1
                    elif key == 'dry':
                        if value == 'O':
                            dry += 1
                        elif value == 'X':
                            dry -= 1
                    else:
                        if value == 'O':
                            sensitive += 1
                        elif value == 'X':
                            sensitive -= 1

                dict={"oilyScore" : oily , "dryScore" : dry, "sensitiveScore" : sensitive}
                product_update = Product.objects.get(id=i['id'])
                product_update.oilyScore = oily
                product_update.dryScore = dry
                product_update.sensitiveScore = sensitive
                product_update.save()

        return Response("success", status=status.HTTP_201_CREATED)


class Intermediary(APIView):

    # def get(self, request, format=None):
    #     # product = Product.objects.filter(connect_ingre__id=2)
    #     # se = ManySerializer(product, many=True)
    #     request.GET['skin_type'] = "asd"
    #     sta = request.GET['skin_type']
    #     str_split = "-" + st + "Score"
    #     return Response(str_split)

    def post(self, request, format=None):
        count = 0
        for data in request.data:
            product = Product.objects.get(id=data['id'])
            list = data['ingredients'].split(',')
            for ingre_list in list:
                ingre = Ingredient.objects.get(name=ingre_list)
                Connect.objects.create(product=product, ingredient=ingre)

        return Response("success", status=status.HTTP_201_CREATED)
