"""
Nome do arquivo: ui_manutencao.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import tkinter as tk
from tkinter import ttk, messagebox
from modules.crud_manutencao import criar, listar, atualizar, deletar

class ManutencaoUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Manutenção")
        self.root.geometry("900x500")

        frame_form = tk.Frame(root)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Máquina ID:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_maquina_id = tk.Entry(frame_form)
        self.entry_maquina_id.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Data:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_data = tk.Entry(frame_form)
        self.entry_data.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_form, text="Descrição:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_descricao = tk.Entry(frame_form, width=50)
        self.entry_descricao.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        tk.Button(frame_form, text="Adicionar", command=self.adicionar).grid(row=2, column=0, padx=10, pady=5)

        columns = ("id", "maquina_id", "data", "descricao")
        self.tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=150)
        self.tree.pack(pady=20)

        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=5)

        tk.Button(frame_buttons, text="Atualizar Lista", command=self.atualizar_lista).grid(row=0, column=0, padx=10)
        tk.Button(frame_buttons, text="Editar", command=self.editar).grid(row=0, column=1, padx=10)
        tk.Button(frame_buttons, text="Deletar", command=self.deletar_registro).grid(row=0, column=2, padx=10)

        self.atualizar_lista()

    def atualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for m in listar():
            self.tree.insert("", "end", values=(m["id"], m["maquina_id"], m["data"], m["descricao"]))

    def adicionar(self):
        maquina_id = self.entry_maquina_id.get().strip()
        data = self.entry_data.get().strip()
        descricao = self.entry_descricao.get().strip()

        if not maquina_id or not data or not descricao:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        criar({"maquina_id": maquina_id, "data": data, "descricao": descricao})
        messagebox.showinfo("Sucesso", "Manutenção adicionada!")
        self.entry_maquina_id.delete(0, tk.END)
        self.entry_data.delete(0, tk.END)
        self.entry_descricao.delete(0, tk.END)
        self.atualizar_lista()

    def editar(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione uma manutenção para editar!")
            return
        id_ = self.tree.item(selected[0])["values"][0]

        maquina_id = self.entry_maquina_id.get().strip()
        data = self.entry_data.get().strip()
        descricao = self.entry_descricao.get().strip()

        if not maquina_id or not data or not descricao:
            messagebox.showwarning("Aviso", "Preencha todos os campos para atualizar!")
            return

        atualizar(id_, {"maquina_id": maquina_id, "data": data, "descricao": descricao})
        messagebox.showinfo("Sucesso", "Manutenção atualizada!")
        self.atualizar_lista()

    def deletar_registro(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione uma manutenção para deletar!")
            return
        id_ = self.tree.item(selected[0])["values"][0]
        deletar(id_)
        messagebox.showinfo("Sucesso", "Manutenção deletada!")
        self.atualizar_lista()
