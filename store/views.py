from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Category, Product, ProductImage
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer



class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImangeViewset(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer