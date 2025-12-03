"""
Nome do arquivo: ui_operacao.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import customtkinter as ctk
from modules.operacao import OperacaoDB

class OperacaoUI(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Operações no Campo")
        self.geometry("600x680")
        self.resizable(False, False)

        ctk.CTkLabel(self, text="Registro de Operações", font=("Arial", 26, "bold")).pack(pady=20)

        self.data_ini = ctk.CTkEntry(self, placeholder_text="Início (AAAA-MM-DD HH:MM)")
        self.data_fim = ctk.CTkEntry(self, placeholder_text="Fim (AAAA-MM-DD HH:MM)")
        self.atividade = ctk.CTkEntry(self, placeholder_text="Atividade (Colheita, Plantio...)")
        self.hor_ini = ctk.CTkEntry(self, placeholder_text="Horímetro Início")
        self.hor_fim = ctk.CTkEntry(self, placeholder_text="Horímetro Fim")
        self.operador = ctk.CTkEntry(self, placeholder_text="Operador")
        self.maquina_id = ctk.CTkEntry(self, placeholder_text="ID Máquina")
        self.cliente_id = ctk.CTkEntry(self, placeholder_text="ID Cliente")

        widgets = [
            self.data_ini, self.data_fim, self.atividade,
            self.hor_ini, self.hor_fim, self.operador,
            self.maquina_id, self.cliente_id
        ]

        for w in widgets:
            w.pack(fill="x", padx=50, pady=10)

        ctk.CTkButton(
            self,
            text="Registrar Operação",
            height=40,
            corner_radius=15,
            command=self.salvar
        ).pack(pady=20)

    def salvar(self):
        dados = [
            self.data_ini.get(),
            self.data_fim.get(),
            self.atividade.get(),
            self.hor_ini.get(),
            self.hor_fim.get(),
            self.operador.get(),
            self.maquina_id.get(),
            self.cliente_id.get()
        ]

        OperacaoDB.salvar(dados)
        self.destroy()
