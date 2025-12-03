"""
Nome do arquivo: crud_maquinas.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import uuid
import os
import json

FILE_PATH = "data/maquinas.txt"

def criar(dados):
    dados["id"] = str(uuid.uuid4())
    with open(FILE_PATH, "a") as f:
        f.write(json.dumps(dados) + "\n")

def listar():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return [json.loads(line.strip()) for line in f if line.strip()]

def atualizar(id_, novos_dados):
    registros = listar()
    with open(FILE_PATH, "w") as f:
        for r in registros:
            if r["id"] == id_:
                r.update(novos_dados)
            f.write(json.dumps(r) + "\n")

def deletar(id_):
    registros = listar()
    with open(FILE_PATH, "w") as f:
        for r in registros:
            if r["id"] != id_:
                f.write(json.dumps(r) + "\n")
