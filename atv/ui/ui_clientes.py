"""
Nome do arquivo: ui_clientes.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import customtkinter as ctk
from modules.clientes import ClientesDB

class ClientesUI(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Cadastro de Clientes / Cooperativas")
        self.geometry("600x550")
        self.resizable(False, False)

        ctk.CTkLabel(self, text="Cadastro de Clientes", font=("Arial", 26, "bold")).pack(pady=20)

        self.nome = ctk.CTkEntry(self, placeholder_text="Nome / Razão Social")
        self.tipo = ctk.CTkEntry(self, placeholder_text="Tipo (Mercado, Cooperativa...)")
        self.cpf_cnpj = ctk.CTkEntry(self, placeholder_text="CPF/CNPJ")
        self.obs = ctk.CTkEntry(self, placeholder_text="Observações")
        self.telefone = ctk.CTkEntry(self, placeholder_text="Telefone")
        self.email = ctk.CTkEntry(self, placeholder_text="E-mail")

        widgets = [
            self.nome, self.tipo, self.cpf_cnpj,
            self.obs, self.telefone, self.email
        ]

        for w in widgets:
            w.pack(fill="x", padx=50, pady=10)

        ctk.CTkButton(
            self,
            text="Salvar Cliente",
            corner_radius=15,
            height=40,
            command=self.salvar
        ).pack(pady=20)

    def salvar(self):
        dados = [
            self.nome.get(),
            self.tipo.get(),
            self.cpf_cnpj.get(),
            self.obs.get(),
            self.telefone.get(),
            self.email.get(),
        ]

        ClientesDB.salvar(dados)
        self.destroy()
