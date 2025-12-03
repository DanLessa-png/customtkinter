"""
Nome do arquivo: ui_insumos.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import customtkinter as ctk
from modules.insumos import InsumosDB

class InsumosUI(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Cadastro de Insumos Agrícolas")
        self.geometry("600x550")
        self.resizable(False, False)

        ctk.CTkLabel(self, text="Cadastro de Insumos", font=("Arial", 26, "bold")).pack(pady=20)

        self.nome = ctk.CTkEntry(self, placeholder_text="Nome do Insumo")
        self.tipo = ctk.CTkEntry(self, placeholder_text="Tipo (Óleo, Filtro, Fertilizante...)")
        self.validade = ctk.CTkEntry(self, placeholder_text="Validade (AAAA-MM-DD)")
        self.quantidade = ctk.CTkEntry(self, placeholder_text="Quantidade")
        self.fornecedor = ctk.CTkEntry(self, placeholder_text="Fornecedor")

        widgets = [
            self.nome, self.tipo, self.validade,
            self.quantidade, self.fornecedor
        ]

        for w in widgets:
            w.pack(fill="x", padx=50, pady=10)

        ctk.CTkButton(
            self,
            text="Salvar Insumo",
            height=40,
            corner_radius=15,
            command=self.salvar
        ).pack(pady=20)

    def salvar(self):
        dados = [
            self.nome.get(),
            self.tipo.get(),
            self.validade.get(),
            self.quantidade.get(),
            self.fornecedor.get()
        ]

        InsumosDB.salvar(dados)
        self.destroy()
