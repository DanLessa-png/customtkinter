"""
Nome do arquivo: operacao.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import os

class OperacaoDB:
    FILE = "data/operacao.txt"

    @staticmethod
    def salvar(op):
        with open(OperacaoDB.FILE, "a", encoding="utf-8") as f:
            f.write(";".join(op) + "\n")

    @staticmethod
    def listar():
        if not os.path.exists(OperacaoDB.FILE):
            return []
        with open(OperacaoDB.FILE, "r", encoding="utf-8") as f:
            return [linha.strip().split(";") for linha in f.readlines()]
