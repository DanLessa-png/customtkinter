"""
Nome do arquivo: maquinas.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import os

class MaquinasDB:
    FILE = "data/maquinas.txt"

    @staticmethod
    def salvar(maquina):
        with open(MaquinasDB.FILE, "a", encoding="utf-8") as f:
            f.write(";".join(maquina) + "\n")

    @staticmethod
    def listar():
        if not os.path.exists(MaquinasDB.FILE):
            return []
        with open(MaquinasDB.FILE, "r", encoding="utf-8") as f:
            return [linha.strip().split(";") for linha in f.readlines()]
