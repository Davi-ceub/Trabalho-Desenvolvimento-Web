# core/services.py
# core/services.py

from .models import *

def registrar_venda(cliente_id, empresa_id, produto_id):
    cliente = Cliente.objects.get(id=cliente_id)
    produto = Produto.objects.get(id=produto_id)
    empresa = Empresa.objects.get(id=empresa_id)

    if produto.quantidade <= 0:
        raise Exception("Produto sem estoque")

    produto.quantidade -= 1
    produto.save()

    venda = Venda.objects.create(
        cliente=cliente,
        empresa=empresa,
        produto=produto,
        valor_total=produto.preco
    )

    return venda