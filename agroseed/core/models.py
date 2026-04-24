# core/models.py
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=13)
    endereco = models.CharField(max_length=200)

class Qualidade(models.Model):
    clima = models.CharField(max_length=75)
    solo = models.CharField(max_length=75)
    resistencia = models.CharField(max_length=75)

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    preco = models.DecimalField(max_digits=9, decimal_places=2)
    quantidade = models.IntegerField()
    qualidade = models.ForeignKey(Qualidade, on_delete=models.CASCADE)

class Empresa(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=250)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

class Venda(models.Model):
    data_compra = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=9, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)