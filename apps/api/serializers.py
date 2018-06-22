from rest_framework import serializers
from .models import ProductType, Category

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductType
        fields = ('url', 'name', 'attributes')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'name', 'product_type')