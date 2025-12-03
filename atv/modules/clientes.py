"""
Nome do arquivo: clientes.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import os

class ClientesDB:
    FILE = "data/clientes.txt"

    @staticmethod
    def salvar(cliente):
        with open(ClientesDB.FILE, "a", encoding="utf-8") as f:
            f.write(";".join(cliente) + "\n")

    @staticmethod
    def listar():
        if not os.path.exists(ClientesDB.FILE):
            return []
        with open(ClientesDB.FILE, "r", encoding="utf-8") as f:
            return [linha.strip().split(";") for linha in f.readlines()]
