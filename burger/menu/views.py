from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView

class CategoryViews(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializars

class BannerView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializers

class StoriesView(ListAPIView):
    queryset = Stories.objects.all()
    serializer_class = StoriesSerializers

class RollView(ListAPIView):
    queryset = Roll.objects.all()
    serializer_class = RollSerializers

@api_view(['GET'])
def Fooddetail(request,food_id):
    foods = get_object_or_404(Food,id=food_id)
    serializer = FoodSerializers(foods,context={'request': request})
    return Response(serializer.data)

@api_view(['POST'])
def CreateOrder(request):
    serializer = OrderCartSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def OrderView(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def Table_create_orderView(request):
    serializer = Tabel_create_orderSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)