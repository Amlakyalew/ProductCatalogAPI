from rest_framework.pagination import PageNumberPagination


class ObjectsListPagination(PageNumberPagination):
    page_size = 10
