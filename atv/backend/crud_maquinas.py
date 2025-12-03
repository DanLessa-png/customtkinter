"""
Nome do arquivo: crud_maquinas.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import os
import uuid

FILE = "data/maquinas.txt"

def criar(maquina: dict):
    if "id" not in maquina:
        maquina["id"] = str(uuid.uuid4())
    with open(FILE, "a", encoding="utf-8") as f:
        linha = f"{maquina['id']};{maquina['tipo']};{maquina['modelo']};{maquina['ano']};{maquina['horimetro']};{maquina['status']}\n"
        f.write(linha)
        return maquina["id"] 

def listar():
    if not os.path.exists(FILE):
        return []
    maquinas = []
    with open(FILE, "r", encoding="utf-8") as f:
        for linha in f:
            id_, tipo, modelo, ano, horimetro, status = linha.strip().split(";")
            maquinas.append({
                "id": id_,
                "tipo": tipo,
                "modelo": modelo,
                "ano": ano,
                "horimetro": horimetro,
                "status": status
            })
    return maquinas

def atualizar(id_, dados: dict):
    linhas = listar()
    with open(FILE, "w", encoding="utf-8") as f:
        for m in linhas:
            if m["id"] == id_:
                m.update(dados)
            f.write(f"{m['id']};{m['tipo']};{m['modelo']};{m['ano']};{m['horimetro']};{m['status']}\n")

def deletar(id_):
    linhas = listar()
    with open(FILE, "w", encoding="utf-8") as f:
        for m in linhas:
            if m["id"] != id_:
                f.write(f"{m['id']};{m['tipo']};{m['modelo']};{m['ano']};{m['horimetro']};{m['status']}\n")
