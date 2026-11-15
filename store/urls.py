from rest_framework.routers import DefaultRouter
from .views import CategoryViewset, ProductViewset

router = DefaultRouter()
router.register('categories', viewset=CategoryViewset)
router.register('products', viewset=ProductViewset)

urlpatterns = router.urls