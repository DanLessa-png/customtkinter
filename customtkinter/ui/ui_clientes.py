"""
Nome do arquivo: ui_clientes.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import tkinter as tk
from tkinter import ttk, messagebox
from modules.crud_clientes import criar, listar, atualizar, deletar

class ClientesUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Clientes")
        self.root.geometry("800x500")

        # Formulário
        frame_form = tk.Frame(root)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nome = tk.Entry(frame_form)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Tipo (Cooperativa/Mercado):").grid(row=0, column=2, padx=5, pady=5)
        self.entry_tipo = tk.Entry(frame_form)
        self.entry_tipo.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_form, text="Contato:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_contato = tk.Entry(frame_form)
        self.entry_contato.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(frame_form, text="Adicionar", command=self.adicionar).grid(row=1, column=2, padx=10, pady=5)

        # Treeview
        columns = ("id", "nome", "tipo", "contato")
        self.tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=150)
        self.tree.pack(pady=20)

        # Botões
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=5)

        tk.Button(frame_buttons, text="Atualizar Lista", command=self.atualizar_lista).grid(row=0, column=0, padx=10)
        tk.Button(frame_buttons, text="Editar", command=self.editar).grid(row=0, column=1, padx=10)
        tk.Button(frame_buttons, text="Deletar", command=self.deletar_registro).grid(row=0, column=2, padx=10)

        self.atualizar_lista()

    def atualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for c in listar():
            self.tree.insert("", "end", values=(c["id"], c["nome"], c["tipo"], c["contato"]))

    def adicionar(self):
        nome = self.entry_nome.get().strip()
        tipo = self.entry_tipo.get().strip()
        contato = self.entry_contato.get().strip()

        if not nome or not tipo or not contato:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        criar({"nome": nome, "tipo": tipo, "contato": contato})
        messagebox.showinfo("Sucesso", "Cliente adicionado!")
        self.entry_nome.delete(0, tk.END)
        self.entry_tipo.delete(0, tk.END)
        self.entry_contato.delete(0, tk.END)
        self.atualizar_lista()

    def editar(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um cliente para editar!")
            return
        id_ = self.tree.item(selected[0])["values"][0]
        nome = self.entry_nome.get().strip()
        tipo = self.entry_tipo.get().strip()
        contato = self.entry_contato.get().strip()

        if not nome or not tipo or not contato:
            messagebox.showwarning("Aviso", "Preencha todos os campos para atualizar!")
            return

        atualizar(id_, {"nome": nome, "tipo": tipo, "contato": contato})
        messagebox.showinfo("Sucesso", "Cliente atualizado!")
        self.atualizar_lista()

    def deletar_registro(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um cliente para deletar!")
            return
        id_ = self.tree.item(selected[0])["values"][0]
        deletar(id_)
        messagebox.showinfo("Sucesso", "Cliente deletado!")
        self.atualizar_lista()
