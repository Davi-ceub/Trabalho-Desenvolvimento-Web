# =============================
# AGROSEED - SISTEMA COMPLETO
# =============================
# Funcionalidades:
# - CRUD Clientes
# - CRUD Produtos
# - Registro de Vendas
# - Controle de Estoque
# - Relatórios
# - Banco SQLite integrado
# - Testes básicos

import sqlite3
from datetime import datetime

# =============================
# BANCO DE DADOS
# =============================
conn = sqlite3.connect('agroseed.db')
cursor = conn.cursor()

# Tabelas
cursor.execute("""
CREATE TABLE IF NOT EXISTS cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cpf TEXT,
    email TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    preco REAL,
    quantidade INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS venda (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    data TEXT,
    total REAL,
    FOREIGN KEY(cliente_id) REFERENCES cliente(id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS venda_produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    venda_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER,
    FOREIGN KEY(venda_id) REFERENCES venda(id),
    FOREIGN KEY(produto_id) REFERENCES produto(id)
)
""")

conn.commit()

# =============================
# CRUD CLIENTE
# =============================
def criar_cliente(nome, cpf, email):
    cursor.execute("INSERT INTO cliente (nome, cpf, email) VALUES (?, ?, ?)", (nome, cpf, email))
    conn.commit()


def listar_clientes():
    return cursor.execute("SELECT * FROM cliente").fetchall()


def atualizar_cliente(id, nome, cpf, email):
    cursor.execute("UPDATE cliente SET nome=?, cpf=?, email=? WHERE id=?", (nome, cpf, email, id))
    conn.commit()


def deletar_cliente(id):
    cursor.execute("DELETE FROM cliente WHERE id=?", (id,))
    conn.commit()

# =============================
# CRUD PRODUTO
# =============================
def criar_produto(nome, preco, quantidade):
    cursor.execute("INSERT INTO produto (nome, preco, quantidade) VALUES (?, ?, ?)", (nome, preco, quantidade))
    conn.commit()


def listar_produtos():
    return cursor.execute("SELECT * FROM produto").fetchall()


def atualizar_produto(id, nome, preco, quantidade):
    cursor.execute("UPDATE produto SET nome=?, preco=?, quantidade=? WHERE id=?", (nome, preco, quantidade, id))
    conn.commit()


def deletar_produto(id):
    cursor.execute("DELETE FROM produto WHERE id=?", (id,))
    conn.commit()

# =============================
# REGISTRO DE VENDA
# =============================
def registrar_venda(cliente_id, itens):
    total = 0

    for produto_id, qtd in itens:
        produto = cursor.execute("SELECT preco, quantidade FROM produto WHERE id=?", (produto_id,)).fetchone()
        if produto is None:
            print("Produto não encontrado")
            return
        preco, estoque = produto

        if estoque < qtd:
            print("Estoque insuficiente")
            return

        total += preco * qtd

    # Criar venda
    cursor.execute("INSERT INTO venda (cliente_id, data, total) VALUES (?, ?, ?)",
                   (cliente_id, datetime.now().strftime("%Y-%m-%d"), total))
    venda_id = cursor.lastrowid

    # Inserir produtos e atualizar estoque
    for produto_id, qtd in itens:
        cursor.execute("INSERT INTO venda_produto (venda_id, produto_id, quantidade) VALUES (?, ?, ?)",
                       (venda_id, produto_id, qtd))

        cursor.execute("UPDATE produto SET quantidade = quantidade - ? WHERE id=?", (qtd, produto_id))

    conn.commit()
    print("Venda registrada com sucesso!")

# =============================
# RELATÓRIOS
# =============================
def relatorio_vendas():
    vendas = cursor.execute("SELECT * FROM venda").fetchall()
    for v in vendas:
        print(f"Venda {v[0]} | Cliente {v[1]} | Data {v[2]} | Total {v[3]}")


def relatorio_estoque():
    produtos = listar_produtos()
    for p in produtos:
        print(f"Produto: {p[1]} | Estoque: {p[3]}")

# =============================
# TESTES BÁSICOS
# =============================
def testes():
    print("\n--- TESTES ---")

    criar_cliente("João", "12345678900", "joao@email.com")
    criar_produto("Soja A", 100.0, 50)
    criar_produto("Soja B", 150.0, 30)

    clientes = listar_clientes()
    produtos = listar_produtos()

    print("Clientes:", clientes)
    print("Produtos:", produtos)

    registrar_venda(clientes[0][0], [(produtos[0][0], 2)])

    relatorio_vendas()
    relatorio_estoque()

# =============================
# EXECUÇÃO
# =============================
if __name__ == "__main__":
    testes()

# =============================
# README (RESUMO)
# =============================
"""
# AgroSeed - Sistema Python

## Funcionalidades
- CRUD de Clientes
- CRUD de Produtos
- Registro de Vendas
- Controle de Estoque
- Relatórios

## Como executar
python app.py

## Banco
SQLite integrado (agroseed.db)

## Testes
Executados automaticamente ao rodar o sistema
"""
