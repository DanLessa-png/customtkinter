"""
Nome do arquivo: crud_manutencao.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import os
import uuid

FILE = "data/manutencao.txt"

def criar(manutencao: dict):
    if "id" not in manutencao:
        manutencao["id"] = str(uuid.uuid4())
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(f"{manutencao['id']};{manutencao['desc']};{manutencao['data_ent']};{manutencao['data_saida']};{manutencao['solic']};{manutencao['tecnico']};{manutencao['maquina_id']}\n")
    return manutencao["id"]

def listar():
    if not os.path.exists(FILE):
        return []
    manutencoes = []
    with open(FILE, "r", encoding="utf-8") as f:
        for linha in f:
            id_, desc, data_ent, data_saida, solic, tecnico, maquina_id = linha.strip().split(";")
            manutencoes.append({"id": id_, "desc": desc, "data_ent": data_ent, "data_saida": data_saida, "solic": solic, "tecnico": tecnico, "maquina_id": maquina_id})
    return manutencoes

def atualizar(id_, dados: dict):
    linhas = listar()
    with open(FILE, "w", encoding="utf-8") as f:
        for m in linhas:
            if m["id"] == id_:
                m.update(dados)
            f.write(f"{m['id']};{m['desc']};{m['data_ent']};{m['data_saida']};{m['solic']};{m['tecnico']};{m['maquina_id']}\n")

def deletar(id_):
    linhas = listar()
    with open(FILE, "w", encoding="utf-8") as f:
        for m in linhas:
            if m["id"] != id_:
                f.write(f"{m['id']};{m['desc']};{m['data_ent']};{m['data_saida']};{m['solic']};{m['tecnico']};{m['maquina_id']}\n")
