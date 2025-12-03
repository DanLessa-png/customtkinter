"""
Nome do arquivo: crud_insumos.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import os
import uuid

FILE = "data/insumos.txt"

def criar(insumo: dict):
    if "id" not in insumo:
        insumo["id"] = str(uuid.uuid4())
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(f"{insumo['id']};{insumo['nome']};{insumo['tipo']};{insumo['validade']};{insumo['quantidade']};{insumo['fornecedor']}\n")
    return insumo["id"]

def listar():
    if not os.path.exists(FILE):
        return []
    insumos = []
    with open(FILE, "r", encoding="utf-8") as f:
        for linha in f:
            id_, nome, tipo, validade, quantidade, fornecedor = linha.strip().split(";")
            insumos.append({"id": id_, "nome": nome, "tipo": tipo, "validade": validade, "quantidade": quantidade, "fornecedor": fornecedor})
    return insumos

def atualizar(id_, dados: dict):
    linhas = listar()
    with open(FILE, "w", encoding="utf-8") as f:
        for i in linhas:
            if i["id"] == id_:
                i.update(dados)
            f.write(f"{i['id']};{i['nome']};{i['tipo']};{i['validade']};{i['quantidade']};{i['fornecedor']}\n")

def deletar(id_):
    linhas = listar()
    with open(FILE, "w", encoding="utf-8") as f:
        for i in linhas:
            if i["id"] != id_:
                f.write(f"{i['id']};{i['nome']};{i['tipo']};{i['validade']};{i['quantidade']};{i['fornecedor']}\n")
