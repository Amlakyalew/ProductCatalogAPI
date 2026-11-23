from django.urls import path, include
from rest_framework_nested import routers
from .views import (
    CategoryViewset,
    ProductViewset,
    ProductImageViewset,
    ManageProductImageViewset,
    StatsViewset,
)

router = routers.DefaultRouter()
router.register("categories", viewset=CategoryViewset)
router.register("products", viewset=ProductViewset)
router.register("images", viewset=ManageProductImageViewset)
router.register("stats", viewset=StatsViewset, basename="stats")


product_router = routers.NestedDefaultRouter(router, "products", lookup="product")
product_router.register(
    "images", viewset=ProductImageViewset, basename="product-images"
)

urlpatterns = [path("", include(router.urls)), path("", include(product_router.urls))]
