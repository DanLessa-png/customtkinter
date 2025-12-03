"""
Nome do arquivo: ui_fluxo_operacao.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import tkinter as tk
from tkinter import ttk, messagebox
from modules.crud_fluxo_operacao import criar, listar, atualizar, deletar

class FluxoOperacaoUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fluxo de Entrada e Saída")
        self.root.geometry("950x500")

        frame_form = tk.Frame(root)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Máquina ID:").grid(row=0, column=0)
        self.entry_maquina = tk.Entry(frame_form)
        self.entry_maquina.grid(row=0, column=1)

        tk.Label(frame_form, text="Data Entrada:").grid(row=0, column=2)
        self.entry_entrada = tk.Entry(frame_form)
        self.entry_entrada.grid(row=0, column=3)

        tk.Label(frame_form, text="Data Saída:").grid(row=1, column=0)
        self.entry_saida = tk.Entry(frame_form)
        self.entry_saida.grid(row=1, column=1)

        tk.Label(frame_form, text="Operador:").grid(row=1, column=2)
        self.entry_operador = tk.Entry(frame_form)
        self.entry_operador.grid(row=1, column=3)

        tk.Button(frame_form, text="Adicionar", command=self.adicionar).grid(row=2, column=0, padx=5, pady=5)

        columns = ("id", "maquina", "entrada", "saida", "operador")
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
        for f in listar():
            self.tree.insert("", "end", values=(f["id"], f["maquina"], f["entrada"], f["saida"], f["operador"]))

    def adicionar(self):
        m = self.entry_maquina.get().strip()
        e = self.entry_entrada.get().strip()
        s = self.entry_saida.get().strip()
        op = self.entry_operador.get().strip()
        if not m or not e or not s or not op:
            messagebox.showwarning("Aviso","Preencha todos os campos!")
            return
        criar({"maquina": m,"entrada":e,"saida":s,"operador":op})
        messagebox.showinfo("Sucesso","Registro adicionado!")
        self.entry_maquina.delete(0,tk.END)
        self.entry_entrada.delete(0,tk.END)
        self.entry_saida.delete(0,tk.END)
        self.entry_operador.delete(0,tk.END)
        self.atualizar_lista()

    def editar(self):
        selected = self.tree.selection()
        if not selected: messagebox.showwarning("Aviso","Selecione para editar"); return
        id_ = self.tree.item(selected[0])["values"][0]
        m = self.entry_maquina.get().strip()
        e = self.entry_entrada.get().strip()
        s = self.entry_saida.get().strip()
        op = self.entry_operador.get().strip()
        if not m or not e or not s or not op:
            messagebox.showwarning("Aviso","Preencha todos os campos!"); return
        atualizar(id_, {"maquina": m,"entrada": e,"saida": s,"operador": op})
        messagebox.showinfo("Sucesso","Registro atualizado!")
        self.atualizar_lista()

    def deletar_registro(self):
        selected = self.tree.selection()
        if not selected: messagebox.showwarning("Aviso","Selecione para deletar"); return
        id_ = self.tree.item(selected[0])["values"][0]
        deletar(id_)
        messagebox.showinfo("Sucesso","Registro deletado!")
        self.atualizar_lista()
