from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework.parsers import JSONParser
import datetime
from .serializers import *
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.db.models import Q
from myapp.item.models import *
import json
from .funtion import ImageParse

price_order = 'price' #정렬-오름차순-가격

class Products(APIView):
    permission_classes = []

    def get(self, request, format=None):
        category = request.GET.get("category", "") #카테고리 파라미
        get_exclude_ingre = request.GET.get('exclude_ingredient',"").split(',') #제외 성분 리스트
        get_include_ingre = request.GET.get('include_ingredient',"").split(',') #필수 성분 리스트
        skin_descending_order = "-" +request.GET['skin_type'] + "Score" #정렬-내림차순-스킨 타입

        #페이징
        last_index = int(request.GET.get("page", 1)) * 50
        begin_item = last_index - 50

        if get_include_ingre[0] == "": #필수 성분 파라미터 X
            if category == "": #카테고리 파라미터 X
                products_obj = Product.objects.\
                all().\
                order_by(skin_descending_order,price_order)
                # exclude(connect_ingre__name__in=get_exclude_ingre)
            else: #카테고리 파라미터 O
                products_obj = Product.objects.\
                all().\
                order_by(skin_descending_order,price_order).\
                filter(category=category)
                # exclude(connect_ingre__name__in=get_exclude_ingre)

        else: #필수 성분 파라미터 O
            if category == "": #카테고리 파라미터 X
                products_obj = Product.objects.\
                filter(connect_ingre__name__in=get_include_ingre).\
                order_by(skin_descending_order,price_order)
                # exclude(connect_ingre__name__in=get_exclude_ingre)
            else: #카테고리 파라미터 O
                products_obj = Product.objects.\
                filter(connect_ingre__name__in=get_include_ingre, category=category).\
                order_by(skin_descending_order,price_order)
                # exclude(connect_ingre__name__in=get_exclude_ingre)

        serial_products = ProductListSerializer(products_obj[begin_item:last_index], many = True)

        #이미지 Url combine
        size = len(serial_products.data)
        for count in range(size):
            serial_products.data[count]['imageUrl'] = ImageParse.thumbnailImage(self,serial_products.data[count]['imageUrl'])

        return Response(serial_products.data)
        # return Response(get_exclude)


class ProductDetail(APIView):

    def get_object(self, pk):
        return get_object_or_404(Product,id=pk)


    def get(self, request, pk, format=None):
        detail_obj = self.get_object(pk)
        category = detail_obj.category
        skin_descending_order = "-" +request.GET['skin_type'] + "Score"

        recommend_obj = Product.objects.\
        filter(category=category).\
        order_by(skin_descending_order,price_order)[0:3]

        detail_serial = ProductDetailSerializer(detail_obj)
        detail_to_string = json.dumps(detail_serial.data)
        detail_dict = json.loads(detail_to_string)
        detail_dict['imageUrl'] = ImageParse.fullImage(self,detail_dict['imageUrl'])

        recommend_serial = ProductRecommendSerializer(recommend_obj, many=True)

        size = len(recommend_serial.data)
        for count in range(size):
            recommend_serial.data[count]['imageUrl']\
            = ImageParse.thumbnailImage(self,recommend_serial.data[count]['imageUrl'])

        re_serial_to_string = json.dumps(recommend_serial.data)
        recommend_dict = json.loads(re_serial_to_string)
        recommend_dict.insert(0,detail_dict)
        return Response(recommend_dict)









    # def get(self, request, format=None):
    #     category = request.GET.get("category", "")
    #     get_exclude_ingre = request.GET.get('exclude_ingredient','').split(',')
    #     get_include_ingre = request.GET.get('include_ingredient','').split(',')
    #
    #     if category == "":
    #         if request.GET['skin_type'] == 'oily':
    #             products_obj = Product.objects.all().order_by('-oilyScore','price')
    #             # products_obj = Product.objects.all(connect_ingre__name__in=get_include_ingre)
    #             # exclude(connect_ingre__name__in=get_exclude_ingre).\
    #         elif request.GET['skin_type'] == 'dry':
    #             products_obj = Product.objects.all().order_by('-dryScore','price').exclude(connect_ingre__name__in=get_exclude_ingre)
    #         elif request.GET['skin_type'] == 'senitive':
    #             products_obj = Product.objects.all().order_by('-sensiScore','price').exclude(connect_ingre__name__in=get_exclude_ingre)
    #     else:
    #         if request.GET['skin_type'] == 'oily':
    #             products_obj = Product.objects.all().order_by('-oilyScore','price').filter(category=category).exclude(connect_ingre__name__in=get_exclude_ingre)
    #         elif request.GET['skin_type'] == 'dry':
    #             products_obj = Product.objects.all().order_by('-dryScore','price').filter(category=category).exclude(connect_ingre__name__in=get_exclude_ingre)
    #         elif request.GET['skin_type'] == 'senitive':
    #             products_obj = Product.objects.all().order_by('-sensiScore','price').filter(category=category).exclude(connect_ingre__name__in=get_exclude_ingre)
    #     # maskpack,basemakeup,suncare,skincare
    #     # if get_exclude_ingre[0] != '':
    #     #     for ex_ingre in get_exclude_ingre:
    #     #         products_obj = products_obj.exclude(ingredients__contain = ex_ingre)
    #     last_index = int(request.GET.get("page", 1)) * 50
    #     begin_item = last_index - 50
    #     serial_products = ManySerializer(products_obj[begin_item:last_index], many = True)
    #
    #     return Response(serial_products.data)
        # return Response(get_exclude)
