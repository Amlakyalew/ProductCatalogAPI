from rest_framework.pagination import PageNumberPagination

class ProductsListPagination(PageNumberPagination):
    page_size = 10