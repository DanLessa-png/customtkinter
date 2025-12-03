"""
Nome do arquivo: ui_manutencao.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import customtkinter as ctk
from modules.manutencao import ManutencaoDB

class ManutencaoUI(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Registro de Manutenções")
        self.geometry("600x650")
        self.resizable(False, False)

        ctk.CTkLabel(self, text="Manutenção de Máquinas", font=("Arial", 26, "bold")).pack(pady=20)

        self.desc = ctk.CTkEntry(self, placeholder_text="Descrição da manutenção")
        self.data_ent = ctk.CTkEntry(self, placeholder_text="Data Entrada (AAAA-MM-DD)")
        self.data_saida = ctk.CTkEntry(self, placeholder_text="Data Saída (AAAA-MM-DD)")
        self.solic = ctk.CTkEntry(self, placeholder_text="Solicitante")
        self.tecnico = ctk.CTkEntry(self, placeholder_text="Técnico Responsável")
        self.maquina_id = ctk.CTkEntry(self, placeholder_text="ID da Máquina")

        widgets = [
            self.desc, self.data_ent, self.data_saida,
            self.solic, self.tecnico, self.maquina_id
        ]

        for w in widgets:
            w.pack(fill="x", padx=50, pady=10)

        ctk.CTkButton(
            self,
            text="Registrar Manutenção",
            height=40,
            corner_radius=15,
            command=self.salvar
        ).pack(pady=20)

    def salvar(self):
        dados = [
            self.desc.get(),
            self.data_ent.get(),
            self.data_saida.get(),
            self.solic.get(),
            self.tecnico.get(),
            self.maquina_id.get()
        ]

        ManutencaoDB.salvar(dados)
        self.destroy()
