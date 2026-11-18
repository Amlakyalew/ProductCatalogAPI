from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Category, Product, ProductImage
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer
from .paginations import ProductsListPagination



class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductsListPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']



class ProductImangeViewset(ModelViewSet):
    serializer_class = ProductImageSerializer

    def get_queryset(self):
        product_id = self.kwargs['product_pk']
        return ProductImage.objects.filter(product_id=product_id)


class ManageProductImageViewset(ModelViewSet):
    http_method_names = ['get', 'delete', 'put']
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()


# class StatsViewset(GenericViewSet):
#     def get_queryset(self):
#         return {"products count": Product.objects.count()}