"""
Nome do arquivo: ui_maquinas.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import tkinter as tk
from tkinter import ttk, messagebox
from modules.crud_maquinas import criar, listar, atualizar, deletar

class MaquinasUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Máquinas")
        self.root.geometry("800x500")

        # Formulário
        frame_form = tk.Frame(root)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Tipo:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_tipo = tk.Entry(frame_form)
        self.entry_tipo.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Modelo:").grid(row=0, column=2, padx=5, pady=5)
        self.entry_modelo = tk.Entry(frame_form)
        self.entry_modelo.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_form, text="Ano:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_ano = tk.Entry(frame_form)
        self.entry_ano.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Horímetro:").grid(row=1, column=2, padx=5, pady=5)
        self.entry_horimetro = tk.Entry(frame_form)
        self.entry_horimetro.grid(row=1, column=3, padx=5, pady=5)

        tk.Label(frame_form, text="Status:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_status = tk.Entry(frame_form)
        self.entry_status.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(frame_form, text="Adicionar", command=self.adicionar).grid(row=2, column=2, padx=10, pady=5)

        # Treeview
        columns = ("id", "tipo", "modelo", "ano", "horimetro", "status")
        self.tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
        for col in columns:
            self.tree.heading(col, text=col.capitalize())
            self.tree.column(col, width=100)
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
        for m in listar():
            self.tree.insert("", "end", values=(m["id"], m["tipo"], m["modelo"], m["ano"], m["horimetro"], m["status"]))

    def adicionar(self):
        tipo = self.entry_tipo.get().strip()
        modelo = self.entry_modelo.get().strip()
        ano = self.entry_ano.get().strip()
        horimetro = self.entry_horimetro.get().strip()
        status = self.entry_status.get().strip()

        if not tipo or not modelo or not ano or not horimetro or not status:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        criar({
            "tipo": tipo,
            "modelo": modelo,
            "ano": ano,
            "horimetro": horimetro,
            "status": status
        })
        messagebox.showinfo("Sucesso", "Máquina adicionada!")
        self.entry_tipo.delete(0, tk.END)
        self.entry_modelo.delete(0, tk.END)
        self.entry_ano.delete(0, tk.END)
        self.entry_horimetro.delete(0, tk.END)
        self.entry_status.delete(0, tk.END)
        self.atualizar_lista()

    def editar(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione uma máquina para editar!")
            return

        id_ = self.tree.item(selected[0])["values"][0]

        tipo = self.entry_tipo.get().strip()
        modelo = self.entry_modelo.get().strip()
        ano = self.entry_ano.get().strip()
        horimetro = self.entry_horimetro.get().strip()
        status = self.entry_status.get().strip()

        if not tipo or not modelo or not ano or not horimetro or not status:
            messagebox.showwarning("Aviso", "Preencha todos os campos para atualizar!")
            return

        atualizar(id_, {
            "tipo": tipo,
            "modelo": modelo,
            "ano": ano,
            "horimetro": horimetro,
            "status": status
        })
        messagebox.showinfo("Sucesso", "Máquina atualizada!")
        self.atualizar_lista()

    def deletar_registro(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione uma máquina para deletar!")
            return
        id_ = self.tree.item(selected[0])["values"][0]
        deletar(id_)
        messagebox.showinfo("Sucesso", "Máquina deletada!")
        self.atualizar_lista()
