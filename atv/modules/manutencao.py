"""
Nome do arquivo: manutencao.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import os

class ManutencaoDB:
    FILE = "data/manutencao.txt"

    @staticmethod
    def salvar(manut):
        with open(ManutencaoDB.FILE, "a", encoding="utf-8") as f:
            f.write(";".join(manut) + "\n")

    @staticmethod
    def listar():
        if not os.path.exists(ManutencaoDB.FILE):
            return []
        with open(ManutencaoDB.FILE, "r", encoding="utf-8") as f:
            return [linha.strip().split(";") for linha in f.readlines()]
