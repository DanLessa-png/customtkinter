"""
Nome do arquivo: pecas.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import window_manager
import json

ARQUIVO = "pecas.txt"

def carregar_dados():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_dados(dados):
    with open(ARQUIVO, "w") as f:
        json.dump(dados, f)

def abrir_janela():
    janela = tk.Toplevel()
    janela.title("AgroManager - Gerenciar Peças/Insumos")
    janela.geometry("1024x768")
    janela.configure(bg='#ecf0f1')
    window_manager.registrar(janela)
    janela.bind('<Escape>', lambda e: janela.destroy())

    
    top_bar = tk.Frame(janela, bg='#1a5f7a', height=60)
    top_bar.pack(fill=tk.X)
    
    def voltar():
        try:
            window_manager.desregistrar()
        finally:
            janela.destroy()
    
    top_inner = tk.Frame(top_bar, bg='#1a5f7a')
    top_inner.pack(expand=True, pady=8)
    ttk.Label(top_inner, text="⚙️ Gerenciar Peças/Insumos", font=("Arial", 14, "bold"), background='#1a5f7a', foreground='white').pack()
    ttk.Button(top_bar, text="← Voltar", command=voltar).pack(side=tk.RIGHT, padx=10, pady=6)
    
    
    main_container = tk.Frame(janela, bg='#ecf0f1')
    main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    
    frame_list = tk.Frame(main_container, bg='#ecf0f1')
    frame_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

    
    tabela = ttk.Treeview(frame_list, columns=('ID', 'Nome', 'Tipo', 'Quantidade'), height=20, show='headings')
    tabela.column('#0', width=0, stretch=tk.NO)
    tabela.column('ID', anchor=tk.CENTER, width=50)
    tabela.column('Nome', anchor=tk.W, width=100)
    tabela.column('Tipo', anchor=tk.W, width=100)
    tabela.column('Quantidade', anchor=tk.CENTER, width=80)
    
    tabela.heading('#0', text='', anchor=tk.W)
    tabela.heading('ID', text='ID')
    tabela.heading('Nome', text='Nome')
    tabela.heading('Tipo', text='Tipo')
    tabela.heading('Quantidade', text='Quantidade')
    
    tabela.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(frame_list, orient=tk.VERTICAL, command=tabela.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tabela.configure(yscroll=scrollbar.set)
    
    
    form_container = tk.Frame(main_container, bg='#ecf0f1')
    form_container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
    
    
    canvas = tk.Canvas(form_container, bg='#ecf0f1', highlightthickness=0, height=400)
    scrollbar_form = tk.Scrollbar(form_container, orient=tk.VERTICAL, command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg='#ecf0f1')
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar_form.set)
    
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar_form.pack(side=tk.RIGHT, fill=tk.Y)

    def atualizar_lista():
        
        for item in tabela.get_children():
            tabela.delete(item)
        
        dados = carregar_dados()
        for item in dados:
            tabela.insert('', tk.END, values=(item['id'], item['nome'], item['tipo'], item['quantidade']))

    atualizar_lista()

    
    frame_form = tk.Frame(scrollable_frame, bg='#ecf0f1')
    frame_form.pack(fill=tk.X, padx=15, pady=10)

    tk.Label(frame_form, text="ID:", bg='#ecf0f1', fg='#333333', font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky=tk.W, pady=5, padx=5)
    id_entry = tk.Entry(frame_form, font=('Arial', 10), bg='white', fg='#333333')
    id_entry.grid(row=0, column=1, sticky=tk.EW, pady=5, padx=5)

    tk.Label(frame_form, text="Nome:", bg='#ecf0f1', fg='#333333', font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)
    nome_entry = tk.Entry(frame_form, font=('Arial', 10), bg='white', fg='#333333')
    nome_entry.grid(row=1, column=1, sticky=tk.EW, pady=5, padx=5)

    tk.Label(frame_form, text="Tipo (ex: filtro, óleo):", bg='#ecf0f1', fg='#333333', font=('Arial', 10, 'bold')).grid(row=2, column=0, sticky=tk.W, pady=5, padx=5)
    tipo_entry = tk.Entry(frame_form, font=('Arial', 10), bg='white', fg='#333333')
    tipo_entry.grid(row=2, column=1, sticky=tk.EW, pady=5, padx=5)

    tk.Label(frame_form, text="Quantidade:", bg='#ecf0f1', fg='#333333', font=('Arial', 10, 'bold')).grid(row=3, column=0, sticky=tk.W, pady=5, padx=5)
    qtd_entry = tk.Entry(frame_form, font=('Arial', 10), bg='white', fg='#333333')
    qtd_entry.grid(row=3, column=1, sticky=tk.EW, pady=5, padx=5)

    frame_form.columnconfigure(1, weight=1)

    def selecionar(event=None):
        sel = tabela.selection()
        if not sel:
            return
        item_id = sel[0]
        valores = tabela.item(item_id)['values']
        id_entry.delete(0, tk.END)
        id_entry.insert(0, valores[0])
        nome_entry.delete(0, tk.END)
        nome_entry.insert(0, valores[1])
        tipo_entry.delete(0, tk.END)
        tipo_entry.insert(0, valores[2])
        qtd_entry.delete(0, tk.END)
        qtd_entry.insert(0, valores[3])

    tabela.bind('<<TreeviewSelect>>', selecionar)

    def criar():
        dados = carregar_dados()
        novo = {
            "id": id_entry.get(),
            "nome": nome_entry.get(),
            "tipo": tipo_entry.get(),
            "quantidade": qtd_entry.get()
        }
        dados.append(novo)
        salvar_dados(dados)
        atualizar_lista()
        messagebox.showinfo("Peça criada", f"Peça '{novo['nome']}' (ID: {novo['id']}) criada com sucesso.")

    def atualizar():
        dados = carregar_dados()
        for item in dados:
            if item["id"] == id_entry.get():
                item.update({
                    "nome": nome_entry.get(),
                    "tipo": tipo_entry.get(),
                    "quantidade": qtd_entry.get()
                })
                salvar_dados(dados)
                atualizar_lista()
                messagebox.showinfo("Peça atualizada", f"Peça '{item.get('nome','')}' (ID: {item.get('id','')}) atualizada com sucesso.")
                return
        messagebox.showerror("Erro - Atualizar", f"ID '{id_entry.get()}' não encontrado.")

    def deletar():
        if not messagebox.askyesno("Confirmar remoção", f"Deseja realmente deletar a peça com ID '{id_entry.get()}'?"):
            return
        dados = carregar_dados()
        dados = [item for item in dados if item["id"] != id_entry.get()]
        salvar_dados(dados)
        atualizar_lista()
        messagebox.showinfo("Peça deletada", f"Peça com ID '{id_entry.get()}' deletada com sucesso.")

    frame_buttons = tk.Frame(scrollable_frame, bg='#ecf0f1')
    frame_buttons.pack(pady=12, expand=True)
    ttk.Button(frame_buttons, text="✅ Criar", command=criar).pack(side=tk.LEFT, padx=8)
    ttk.Button(frame_buttons, text="🔄 Atualizar", command=atualizar).pack(side=tk.LEFT, padx=8)
    ttk.Button(frame_buttons, text="🗑️ Deletar", command=deletar).pack(side=tk.LEFT, padx=8)