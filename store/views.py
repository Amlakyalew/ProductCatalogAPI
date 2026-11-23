from decimal import Decimal, ROUND_HALF_UP
from django.db.models import Avg, Count
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated, SAFE_METHODS
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Category, Product, ProductImage
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer
from .paginations import ObjectsListPagination


class CategoryViewset(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAuthenticated()]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = ObjectsListPagination


class ProductViewset(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAuthenticated()]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ObjectsListPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]


class ProductImageViewset(viewsets.ModelViewSet):
    serializer_class = ProductImageSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAuthenticated()]

    def get_queryset(self):
        product_id = self.kwargs["product_pk"]
        return ProductImage.objects.filter(product_id=product_id)


class ManageProductImageViewset(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [AllowAny()]
        return [IsAuthenticated()]

    http_method_names = ["get", "delete", "put"]
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()


class StatsViewset(viewsets.ViewSet):

    @action(detail=False, methods=["get"])
    def total_products(self, request):
        return Response({"total_products": Product.objects.count()})

    @action(detail=False, methods=["get"])
    def products_per_category(self, request):
        categories = Category.objects.annotate(products_amt=Count("products"))
        results = {}

        for category in categories:
            results[category.name] = category.products_amt
        return Response(results)

    @action(detail=False, methods=["get"])
    def avg_price_per_category(self, request):
        categories = Category.objects.annotate(avg_price=Avg("products__price"))
        result = {}

        for category in categories:
            if category.avg_price is not None:
                result[category.name] = (category.avg_price).quantize(
                    Decimal("0.01"), ROUND_HALF_UP
                )
            else:
                result[category.name] = Decimal("0.00")
        return Response(result)
