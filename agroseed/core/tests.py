# core/tests.py
from django.test import TestCase
from .models import Produto

class ProdutoTest(TestCase):

    def test_criar_produto(self):
        produto = Produto.objects.create(
            nome="Soja X",
            descricao="Teste",
            preco=100,
            quantidade=10,
            qualidade_id=1
        )
        self.assertEqual(produto.nome, "Soja X")