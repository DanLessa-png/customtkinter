"""
Nome do arquivo: crud_clientes.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import os
import uuid

FILE = "data/clientes.txt"

def criar(cliente: dict):
    if "id" not in cliente:
        cliente["id"] = str(uuid.uuid4())
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(f"{cliente['id']};{cliente['nome']};{cliente['tipo']};{cliente['cpf_cnpj']};{cliente['telefone']};{cliente['email']}\n")
    return cliente["id"]

def listar():
    if not os.path.exists(FILE):
        return []
    clientes = []
    with open(FILE, "r", encoding="utf-8") as f:
        for linha in f:
            id_, nome, tipo, cpf_cnpj, telefone, email = linha.strip().split(";")
            clientes.append({"id": id_, "nome": nome, "tipo": tipo, "cpf_cnpj": cpf_cnpj, "telefone": telefone, "email": email})
    return clientes

def atualizar(id_, dados: dict):
    linhas = listar()
    with open(FILE, "w", encoding="utf-8") as f:
        for c in linhas:
            if c["id"] == id_:
                c.update(dados)
            f.write(f"{c['id']};{c['nome']};{c['tipo']};{c['cpf_cnpj']};{c['telefone']};{c['email']}\n")

def deletar(id_):
    linhas = listar()
    with open(FILE, "w", encoding="utf-8") as f:
        for c in linhas:
            if c["id"] != id_:
                f.write(f"{c['id']};{c['nome']};{c['tipo']};{c['cpf_cnpj']};{c['telefone']};{c['email']}\n")
