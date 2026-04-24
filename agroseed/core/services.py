# core/services.py
from .models import Venda, Produto

def registrar_venda(cliente, empresa, produto_id):
    produto = Produto.objects.get(id=produto_id)

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