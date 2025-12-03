"""
Nome do arquivo: insumos.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import os

class InsumosDB:
    FILE = "data/insumos.txt"

    @staticmethod
    def salvar(insumo):
        with open(InsumosDB.FILE, "a", encoding="utf-8") as f:
            f.write(";".join(insumo) + "\n")

    @staticmethod
    def listar():
        if not os.path.exists(InsumosDB.FILE):
            return []
        with open(InsumosDB.FILE, "r", encoding="utf-8") as f:
            return [linha.strip().split(";") for linha in f.readlines()]
