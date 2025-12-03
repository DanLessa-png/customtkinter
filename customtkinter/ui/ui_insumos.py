"""
Nome do arquivo: ui_insumos.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import tkinter as tk
from tkinter import ttk, messagebox
from modules.crud_insumos import criar, listar, atualizar, deletar

class InsumosUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Insumos")
        self.root.geometry("800x500")

        # Formulário
        frame_form = tk.Frame(root)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nome = tk.Entry(frame_form)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Tipo (Filtro/Óleo/Peça):").grid(row=0, column=2, padx=5, pady=5)
        self.entry_tipo = tk.Entry(frame_form)
        self.entry_tipo.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_form, text="Quantidade:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_quantidade = tk.Entry(frame_form)
        self.entry_quantidade.grid(row=1, column=1, padx=5, pady=5)

        tk.Button(frame_form, text="Adicionar", command=self.adicionar).grid(row=1, column=2, padx=10, pady=5)

        # Treeview
        columns = ("id", "nome", "tipo", "quantidade")
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
        for i in listar():
            self.tree.insert("", "end", values=(i["id"], i["nome"], i["tipo"], i["quantidade"]))

    def adicionar(self):
        nome = self.entry_nome.get().strip()
        tipo = self.entry_tipo.get().strip()
        quantidade = self.entry_quantidade.get().strip()

        if not nome or not tipo or not quantidade:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        criar({"nome": nome, "tipo": tipo, "quantidade": quantidade})
        messagebox.showinfo("Sucesso", "Insumo adicionado!")
        self.entry_nome.delete(0, tk.END)
        self.entry_tipo.delete(0, tk.END)
        self.entry_quantidade.delete(0, tk.END)
        self.atualizar_lista()

    def editar(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um insumo para editar!")
            return
        id_ = self.tree.item(selected[0])["values"][0]
        nome = self.entry_nome.get().strip()
        tipo = self.entry_tipo.get().strip()
        quantidade = self.entry_quantidade.get().strip()

        if not nome or not tipo or not quantidade:
            messagebox.showwarning("Aviso", "Preencha todos os campos para atualizar!")
            return

        atualizar(id_, {"nome": nome, "tipo": tipo, "quantidade": quantidade})
        messagebox.showinfo("Sucesso", "Insumo atualizado!")
        self.atualizar_lista()

    def deletar_registro(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um insumo para deletar!")
            return
        id_ = self.tree.item(selected[0])["values"][0]
        deletar(id_)
        messagebox.showinfo("Sucesso", "Insumo deletado!")
        self.atualizar_lista()
