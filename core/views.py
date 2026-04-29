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


from django.shortcuts import render, redirect
from .models import *
from .services import registrar_venda

from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def clientes_view(request):
    if request.method == 'POST':
        Cliente.objects.create(
            nome=request.POST['nome'],
            cpf=request.POST['cpf'],
            email="teste@email.com",
            telefone="000",
            endereco="teste"
        )
        return redirect('clientes')

    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})


def produtos_view(request):
    if request.method == 'POST':
        qualidade = Qualidade.objects.first()  # 👈 pega qualquer qualidade

        if not qualidade:
            return render(request, 'produtos.html', {
                'produtos': Produto.objects.all(),
                'erro': 'Cadastre uma qualidade primeiro'
            })

        Produto.objects.create(
            nome=request.POST['nome'],
            preco=request.POST['preco'],
            quantidade=request.POST['quantidade'],
            descricao="teste",
            qualidade=qualidade  # 👈 CORRETO
        )
        return redirect('produtos')

    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

def vendas_view(request):
    if request.method == 'POST':
        empresa = Empresa.objects.first()  # 👈 define empresa

        if not empresa:
            return render(request, 'vendas.html', {
                'clientes': Cliente.objects.all(),
                'produtos': Produto.objects.all(),
                'vendas': Venda.objects.all(),
                'erro': 'Cadastre uma empresa primeiro'
            })

        registrar_venda(
            cliente_id=request.POST['cliente'],
            empresa=empresa,  # 👈 CORRETO
            produto_id=request.POST['produto']
        )
        return redirect('vendas')

    context = {
        'clientes': Cliente.objects.all(),
        'produtos': Produto.objects.all(),
        'vendas': Venda.objects.all()
    }

    return render(request, 'vendas.html', context)

def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)

    if request.method == 'POST':
        cliente.nome = request.POST.get('nome')
        cliente.cpf = request.POST.get('cpf')
        cliente.email = request.POST.get('email')
        cliente.save()
        return redirect('clientes')

    return render(request, 'editar_cliente.html', {'cliente': cliente})

def deletar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('clientes')

def editar_produto(request, id):
    produto = Produto.objects.get(id=id)

    if request.method == 'POST':
        produto.nome = request.POST.get('nome')
        produto.preco = request.POST.get('preco')
        produto.quantidade = request.POST.get('quantidade')
        produto.save()
        return redirect('produtos')

    return render(request, 'editar_produto.html', {'produto': produto})

def deletar_produto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect('produtos')