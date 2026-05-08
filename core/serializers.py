# core/serializers.py

from rest_framework import serializers
from .models import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'