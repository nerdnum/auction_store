from django.urls import path, include
from .views import ProductTypeList, ProductTypeDetail, CategoryList, CategoryDetail

urlpatterns = [
    path('product-type/', ProductTypeList.as_view(), name=ProductTypeList.name),
    path('product-type-detail/<slug:slug>/', ProductTypeDetail.as_view(), name=ProductTypeDetail.name),
    path('category-list/', CategoryList.as_view(), name=CategoryList.name),
    path('category-detail/<slug:slug>/', CategoryDetail.as_view(), name=CategoryDetail.name),
]