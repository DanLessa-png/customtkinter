"""
Nome do arquivo: ui_operacao.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import tkinter as tk
from tkinter import ttk, messagebox
from modules.crud_operacao import criar, listar, atualizar, deletar

class OperacaoUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Operações de Máquinas")
        self.root.geometry("900x500")

        frame_form = tk.Frame(root)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Máquina ID:").grid(row=0, column=0)
        self.entry_maquina = tk.Entry(frame_form)
        self.entry_maquina.grid(row=0, column=1)

        tk.Label(frame_form, text="Data:").grid(row=0, column=2)
        self.entry_data = tk.Entry(frame_form)
        self.entry_data.grid(row=0, column=3)

        tk.Label(frame_form, text="Operador:").grid(row=1, column=0)
        self.entry_operador = tk.Entry(frame_form)
        self.entry_operador.grid(row=1, column=1)

        tk.Label(frame_form, text="Descrição:").grid(row=1, column=2)
        self.entry_desc = tk.Entry(frame_form, width=40)
        self.entry_desc.grid(row=1, column=3)

        tk.Button(frame_form, text="Adicionar", command=self.adicionar).grid(row=2, column=0, padx=5, pady=5)

        columns = ("id", "maquina", "data", "operador", "descricao")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=150)
        self.tree.pack(pady=20)

        frame_buttons = tk.Frame(root)
        frame_buttons.pack()
        tk.Button(frame_buttons, text="Atualizar Lista", command=self.atualizar_lista).grid(row=0, column=0)
        tk.Button(frame_buttons, text="Editar", command=self.editar).grid(row=0, column=1)
        tk.Button(frame_buttons, text="Deletar", command=self.deletar_registro).grid(row=0, column=2)

        self.atualizar_lista()

    def atualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for o in listar():
            self.tree.insert("", "end", values=(o["id"], o["maquina"], o["data"], o["operador"], o["descricao"]))

    def adicionar(self):
        m = self.entry_maquina.get().strip()
        d = self.entry_data.get().strip()
        op = self.entry_operador.get().strip()
        desc = self.entry_desc.get().strip()
        if not m or not d or not op or not desc:
            messagebox.showwarning("Aviso","Preencha todos os campos!")
            return
        criar({"maquina": m,"data":d,"operador":op,"descricao":desc})
        messagebox.showinfo("Sucesso","Operação adicionada!")
        self.entry_maquina.delete(0,tk.END)
        self.entry_data.delete(0,tk.END)
        self.entry_operador.delete(0,tk.END)
        self.entry_desc.delete(0,tk.END)
        self.atualizar_lista()

    def editar(self):
        selected = self.tree.selection()
        if not selected: messagebox.showwarning("Aviso","Selecione para editar"); return
        id_ = self.tree.item(selected[0])["values"][0]
        m = self.entry_maquina.get().strip()
        d = self.entry_data.get().strip()
        op = self.entry_operador.get().strip()
        desc = self.entry_desc.get().strip()
        if not m or not d or not op or not desc:
            messagebox.showwarning("Aviso","Preencha todos os campos!"); return
        atualizar(id_, {"maquina": m,"data":d,"operador":op,"descricao":desc})
        messagebox.showinfo("Sucesso","Operação atualizada!")
        self.atualizar_lista()

    def deletar_registro(self):
        selected = self.tree.selection()
        if not selected: messagebox.showwarning("Aviso","Selecione para deletar"); return
        id_ = self.tree.item(selected[0])["values"][0]
        deletar(id_)
        messagebox.showinfo("Sucesso","Operação deletada!")
        self.atualizar_lista()
