"""
Nome do arquivo: crud_operacao.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import os
import uuid

FILE = "data/operacao.txt"

def criar(operacao: dict):
    if "id" not in operacao:
        operacao["id"] = str(uuid.uuid4())
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(f"{operacao['id']};{operacao['data_ini']};{operacao['data_fim']};{operacao['atividade']};{operacao['hor_ini']};{operacao['hor_fim']};{operacao['operador']};{operacao['maquina_id']};{operacao['cliente_id']}\n")
    return operacao["id"]

def listar():
    if not os.path.exists(FILE):
        return []
    operacoes = []
    with open(FILE, "r", encoding="utf-8") as f:
        for linha in f:
            id_, data_ini, data_fim, atividade, hor_ini, hor_fim, operador, maquina_id, cliente_id = linha.strip().split(";")
            operacoes.append({"id": id_, "data_ini": data_ini, "data_fim": data_fim, "atividade": atividade, "hor_ini": hor_ini, "hor_fim": hor_fim, "operador": operador, "maquina_id": maquina_id, "cliente_id": cliente_id})
    return operacoes

def atualizar(id_, dados: dict):
    linhas = listar()
    with open(FILE, "w", encoding="utf-8") as f:
        for o in linhas:
            if o["id"] == id_:
                o.update(dados)
            f.write(f"{o['id']};{o['data_ini']};{o['data_fim']};{o['atividade']};{o['hor_ini']};{o['hor_fim']};{o['operador']};{o['maquina_id']};{o['cliente_id']}\n")

def deletar(id_):
    linhas = listar()
    with open(FILE, "w", encoding="utf-8") as f:
        for o in linhas:
            if o["id"] != id_:
                f.write(f"{o['id']};{o['data_ini']};{o['data_fim']};{o['atividade']};{o['hor_ini']};{o['hor_fim']};{o['operador']};{o['maquina_id']};{o['cliente_id']}\n")
