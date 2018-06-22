from django.shortcuts import render
from .models import ProductType, Category
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import ProductTypeSerializer, CategorySerializer
# Create your views here.

class ProductTypeList(generics.ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    name = 'product-type-list'

class ProductTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    name = 'product-type-detail'

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *arg, **kwargs):
        return Response({
            'product-types': reverse(ProductTypeList, request= request),
            'catefories': reverse(CategoryList, request= request)
        })