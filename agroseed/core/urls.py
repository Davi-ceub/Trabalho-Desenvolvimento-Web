# core/urls.py
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('produtos', ProdutoViewSet)
router.register('vendas', VendaViewSet)

urlpatterns = router.urls