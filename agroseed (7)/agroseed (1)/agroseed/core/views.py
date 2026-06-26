# =========================================================
# IMPORTS
# =========================================================

from django.shortcuts import render, redirect
from django.db.models import Sum

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *
from .services import registrar_venda


# =========================================================
# API - VIEWSETS
# =========================================================

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAuthenticated]


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def registrar(self, request):

        venda = registrar_venda(
            cliente_id=request.data['cliente'],
            empresa_id=request.data['empresa'],
            produto_id=request.data['produto']
        )

        return Response(VendaSerializer(venda).data)


# =========================================================
# API - RELATÓRIOS
# =========================================================

class RelatorioViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def vendas(self, request):

        total = Venda.objects.aggregate(
            total=Sum('valor_total')
        )

        return Response(total)

    def por_cliente(self, request):

        dados = Venda.objects.values(
            'cliente__nome'
        ).annotate(
            total=Sum('valor_total')
        )

        return Response(dados)


# =========================================================
# PÁGINA INICIAL
# =========================================================

def index(request):
    return render(request, 'index.html')


# =========================================================
# CLIENTES
# =========================================================

def clientes_view(request):

    if request.method == 'POST':

        Cliente.objects.create(
            nome=request.POST['nome'],
            cpf=request.POST['cpf'],
            email='teste@email.com',
            telefone=request.POST['telefone'],
            endereco=request.POST['endereco']
        )

        return redirect('clientes')

    clientes = Cliente.objects.all()

    return render(
        request,
        'clientes.html',
        {'clientes': clientes}
    )


def editar_cliente(request, id):

    cliente = Cliente.objects.get(id=id)

    if request.method == 'POST':

        cliente.nome = request.POST.get('nome')
        cliente.cpf = request.POST.get('cpf')
        cliente.telefone = request.POST.get('telefone')
        cliente.endereco = request.POST.get('endereco')

        cliente.save()

        return redirect('clientes')

    return render(
        request,
        'editar_cliente.html',
        {'cliente': cliente}
    )


def deletar_cliente(request, id):

    cliente = Cliente.objects.get(id=id)

    cliente.delete()

    return redirect('clientes')


# =========================================================
# EMPRESA
# =========================================================

def empresa_view(request):

    if request.method == 'POST':

        Empresa.objects.create(
            nome=request.POST['nome'],
            cnpj=request.POST['cnpj'],
            endereco=request.POST['endereco']
        )

        return redirect('empresa')

    empresa = Empresa.objects.all()

    return render(
        request,
        'empresa.html',
        {'empresa': empresa}
    )


def editar_empresa(request, id):

    empresa = Empresa.objects.get(id=id)

    if request.method == 'POST':

        empresa.nome = request.POST.get('nome')
        empresa.cnpj = request.POST.get('cnpj')
        empresa.endereco = request.POST.get('endereco')

        empresa.save()

        return redirect('empresa')

    return render(
        request,
        'editar_empresa.html',
        {'empresa': empresa}
    )


def deletar_empresa(request, id):

    empresa = Empresa.objects.get(id=id)

    empresa.delete()

    return redirect('empresa')


# =========================================================
# PRODUTOS
# =========================================================

def produtos_view(request):

    if request.method == 'POST':

        Produto.objects.create(
            nome=request.POST['nome'],
            preco=request.POST['preco'],
            quantidade=request.POST['quantidade'],
            descricao='teste'
        )

        return redirect('produtos')

    produtos = Produto.objects.all()

    return render(
        request,
        'produtos.html',
        {'produtos': produtos}
    )


def editar_produto(request, id):

    produto = Produto.objects.get(id=id)

    if request.method == 'POST':

        produto.nome = request.POST.get('nome')
        produto.preco = request.POST.get('preco')
        produto.quantidade = request.POST.get('quantidade')

        produto.save()

        return redirect('produtos')

    return render(
        request,
        'editar_produto.html',
        {'produto': produto}
    )


def deletar_produto(request, id):

    produto = Produto.objects.get(id=id)

    produto.delete()

    return redirect('produtos')


# =========================================================
# VENDAS
# =========================================================

def vendas_view(request):

    if request.method == 'POST':

        empresa = Empresa.objects.first()

        if not empresa:

            return render(request, 'vendas.html', {
                'clientes': Cliente.objects.all(),
                'produtos': Produto.objects.all(),
                'empresas': Empresa.objects.all(),
                'vendas': Venda.objects.all(),
                'erro': 'Cadastre uma empresa primeiro'
            })

        registrar_venda(
            cliente_id=request.POST['cliente'],
            empresa_id=request.POST['empresa'],
            produto_id=request.POST['produto']
        )

        return redirect('vendas')

    context = {
        'clientes': Cliente.objects.all(),
        'produtos': Produto.objects.all(),
        'empresas': Empresa.objects.all(),
        'vendas': Venda.objects.all()
    }

    return render(
        request,
        'vendas.html',
        context
    )