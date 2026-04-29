# core/urls.py
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('produtos', ProdutoViewSet)
router.register('empresa', EmpresaViewSet)
router.register('vendas', VendaViewSet)

urlpatterns = router.urls

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('clientes/', clientes_view, name='clientes'),
    path('produtos/', produtos_view, name='produtos'),
    path('vendas/', vendas_view, name='vendas'),
    path('empresa/', empresa_view, name='empresa'),
    path('clientes/editar/<int:id>/', editar_cliente, name='editar_cliente'),
    path('clientes/deletar/<int:id>/', deletar_cliente, name='deletar_cliente'),
    path('produtos/editar/<int:id>/', editar_produto, name='editar_produto'),
    path('produtos/deletar/<int:id>/', deletar_produto, name='deletar_produto'),
    path('empresa/editar/<int:id>/', editar_empresa, name='editar_empresa'),
    path('empresa/deletar/<int:id>/', deletar_empresa, name='deletar_empresa'),
]