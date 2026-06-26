# core/urls.py

from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

from .views import *


# =========================================================
# API ROUTER
# =========================================================

router = DefaultRouter()

router.register(r'clientes', ClienteViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'empresa', EmpresaViewSet)
router.register(r'vendas', VendaViewSet)


# =========================================================
# URL PATTERNS
# =========================================================

urlpatterns = [

    # =====================================================
    # API
    # =====================================================

    path('api/', include(router.urls)),


    # =====================================================
    # PÁGINAS
    # =====================================================

    path('', index, name='home'),
    path('clientes/', clientes_view, name='clientes'),
    path('produtos/', produtos_view, name='produtos'),
    path('vendas/', vendas_view, name='vendas'),
    path('empresa/', empresa_view, name='empresa'),


    # =====================================================
    # CLIENTES
    # =====================================================

    path(
        'clientes/editar/<int:id>/',
        editar_cliente,
        name='editar_cliente'
    ),

    path(
        'clientes/deletar/<int:id>/',
        deletar_cliente,
        name='deletar_cliente'
    ),


    # =====================================================
    # PRODUTOS
    # =====================================================

    path(
        'produtos/editar/<int:id>/',
        editar_produto,
        name='editar_produto'
    ),

    path(
        'produtos/deletar/<int:id>/',
        deletar_produto,
        name='deletar_produto'
    ),


    # =====================================================
    # EMPRESA
    # =====================================================

    path(
        'empresa/editar/<int:id>/',
        editar_empresa,
        name='editar_empresa'
    ),

    path(
        'empresa/deletar/<int:id>/',
        deletar_empresa,
        name='deletar_empresa'
    ),


    # =====================================================
    # RECUPERAÇÃO DE SENHA
    # =====================================================
    
    path(
    'login/',
    auth_views.LoginView.as_view(
        template_name='login.html'
    ),
    name='login'
),
    
    path(
    'logout/',
    auth_views.LogoutView.as_view(),
    name='logout'
),

    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'
    ),

    path(
        'password_reset_done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),

    path(
        'reset_done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),
]