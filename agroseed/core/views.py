# core/views.py
from rest_framework import viewsets
from .models import *
from .serializers import *
from .services import registrar_venda
from rest_framework.decorators import action
from rest_framework.response import Response

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

    @action(detail=False, methods=['post'])
    def registrar(self, request):
        venda = registrar_venda(
            cliente_id=request.data['cliente'],
            empresa_id=request.data['empresa'],
            produto_id=request.data['produto']
        )
        return Response(VendaSerializer(venda).data)
    
# core/views.py (continuação)

from django.db.models import Sum

class RelatorioViewSet(viewsets.ViewSet):

    def vendas(self, request):
        total = Venda.objects.aggregate(total=Sum('valor_total'))
        return Response(total)

    def por_cliente(self, request):
        dados = Venda.objects.values('cliente__nome').annotate(total=Sum('valor_total'))
        return Response(dados)