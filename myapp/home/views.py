from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.shortcuts import get_object_or_404
from django.http import Http404
from myapp.item.models import *
from .funtion import *


def index(request):
    return render(request, 'index.html', {})



price_order = 'price' #정렬-오름차순-가격
required_key = 'skin_type'
class Products(APIView):
    permission_classes = []

    def get(self, request, format=None):

        #필수 파라미터 키 확인
        try:
            skin_descending_order = "-" +request.GET[required_key] + "Score" #정렬-내림차순-스킨 타입
        except KeyError:
            result = noneRequiredKey(self,required_key,*request.GET.keys())
            return Response(result, status = status.HTTP_400_BAD_REQUEST)

        #필수 파라미터 벨류 확인
        if badRequiredValueCondition(self,request.GET[required_key]):
            bad_value = badRequiredValue(self, request.GET[required_key])
            return Response(bad_value, status = status.HTTP_400_BAD_REQUEST)

        category = request.GET.get("category", "") #카테고리 파라미터
        get_exclude_ingre = request.GET.get('exclude_ingredient',"").split(',') #제외 성분 리스트
        get_include_ingre = request.GET.get('include_ingredient',"").split(',') #필수 성분 리스트

        #페이징 50페이지씩 페이징
        last_index = int(request.GET.get("page", 1)) * 50
        begin_item = last_index - 50

        #공통 쿼리 체이닝
        products_obj = Product.objects.\
        exclude(connect_ingre__name__in=get_exclude_ingre).\
        order_by(skin_descending_order,price_order)

        if get_include_ingre[0] == "": #필수 성분 파라미터 X
            products_obj = products_obj.all()

        else: #필수 성분 파라미터 O
            products_obj = products_obj.filter(connect_ingre__name__in=get_include_ingre)

        if category != "": #카테고리 파라미터 O
            products_obj = products_obj.filter(category=category)


        serial_products = ProductListSerializer(products_obj[begin_item:last_index], many = True)

        #이미지 Url combine
        size = len(serial_products.data)
        for count in range(size):
            serial_products.data[count]['imageUrl']\
             = ImageParse.thumbnailImage(self,serial_products.data[count]['imageUrl'])

        return Response(serial_products.data,status=status.HTTP_200_OK)



class ProductDetail(APIView):
    permission_classes = []
    def get_object(self, pk):
        return get_object_or_404(Product,id=pk)


    def get(self, request, pk, format=None):
        detail_obj = self.get_object(pk) #자세히 보기 객체 가져오기
        try:
            skin_descending_order = "-" +request.GET[required_key] + "Score" #정렬-내림차순-스킨 타입
        except KeyError:
            result = noneRequiredKey(self,required_key,*request.GET.keys())
            return Response(result, status = status.HTTP_400_BAD_REQUEST)

        if badRequiredValueCondition(self,request.GET[required_key]):
            bad_value = badRequiredValue(self, request.GET[required_key])
            return Response(bad_value, status = status.HTTP_400_BAD_REQUEST)

        category = detail_obj.category #하위 목록으로 3개까지 띄워줄 카테고리
        recommend_obj = Product.objects.\
        filter(category=category).\
        order_by(skin_descending_order,price_order)[0:3]

        detail_serial = ProductDetailSerializer(detail_obj)
        detail_dict = jsonDumpsLoads(self,**detail_serial.data)
        detail_dict['imageUrl'] = ImageParse.fullImage(self,detail_dict['imageUrl'])

        recommend_serial = ProductRecommendSerializer(recommend_obj, many=True)

        size = len(recommend_serial.data)
        for count in range(size):
            recommend_serial.data[count]['imageUrl']\
            = ImageParse.thumbnailImage(self,recommend_serial.data[count]['imageUrl'])

        recommend_dict = jsonDumpsLoads(self,*recommend_serial.data)
        recommend_dict.insert(0,detail_dict)
        return Response(recommend_dict,status=status.HTTP_200_OK)
