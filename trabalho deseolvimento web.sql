create database Agronomia;

use Agronomia;

create table cliente(
id int primary key not null auto_increment,
nome varchar(200) not null,
cpf bigint unique not null,
email varchar(50) unique not null,
telefone char(13) null,
endereco varchar(200) unique not null);

create table produto(
id int primary key not null auto_increment,
nome varchar(100) not null,
descricao varchar(250) not null,
preco decimal(9,2) not null,
quantidade varchar(5) not null,
id_qualidade int);

create table empresa(
id int primary key not null auto_increment,
nome varchar(200) not null,
cnpj varchar(14) not null unique,
endereco varchar(250) not null,
id_produto int);

create table venda(
id int primary key not null auto_increment,
dataCompra date not null,
valortotal decimal(9,2) not null,
id_cliente int,
id_empresa int,
id_produtos int);

create table caracteristicas(
id int primary key not null auto_increment,
clima varchar(75) not null,
solo varchar(75) not null,
resistencia varchar(75) not null); 

ALTER TABLE produto
ADD CONSTRAINT fk_produto_caracteristicas
FOREIGN KEY (id_caracteristicas)
REFERENCES caracteristicas(id);

ALTER TABLE empresa
ADD CONSTRAINT fk_empresa_produto
FOREIGN KEY (id_produto)
REFERENCES produto(id);

ALTER TABLE venda
ADD CONSTRAINT fk_venda_cliente
FOREIGN KEY (id_cliente)
REFERENCES cliente(id);

ALTER TABLE venda
ADD CONSTRAINT fk_venda_empresa
FOREIGN KEY (id_empresa)
REFERENCES empresa(id);

ALTER TABLE venda
ADD CONSTRAINT fk_venda_produto
FOREIGN KEY (id_produtos)
REFERENCES produto(id);
