"""
Nome do arquivo: fornecedores.py
Equipe: Dan Lessa e Kevin Anjos
Turma: G93311
Semestre: 2025.2
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import json
import window_manager

ARQUIVO = "fornecedores.txt"

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
    janela.title("AgroManager - Gerenciar Fornecedores")
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
    ttk.Label(top_inner, text="🚚 Gerenciar Fornecedores", font=("Arial", 14, "bold"), background='#1a5f7a', foreground='white').pack()
    ttk.Button(top_bar, text="← Voltar", command=voltar).pack(side=tk.RIGHT, padx=10, pady=6)
    
  
    main_container = tk.Frame(janela, bg='#ecf0f1')
    main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    
    frame_list = tk.Frame(main_container, bg='#ecf0f1')
    frame_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

   
    tabela = ttk.Treeview(frame_list, columns=('ID', 'Nome', 'Contato', 'Rua', 'Bairro', 'Cidade'), height=20, show='headings')
    tabela.column('#0', width=0, stretch=tk.NO)
    tabela.column('ID', anchor=tk.CENTER, width=40)
    tabela.column('Nome', anchor=tk.W, width=80)
    tabela.column('Contato', anchor=tk.W, width=80)
    tabela.column('Rua', anchor=tk.W, width=70)
    tabela.column('Bairro', anchor=tk.W, width=70)
    tabela.column('Cidade', anchor=tk.W, width=70)
    
    tabela.heading('#0', text='', anchor=tk.W)
    tabela.heading('ID', text='ID')
    tabela.heading('Nome', text='Nome')
    tabela.heading('Contato', text='Contato')
    tabela.heading('Rua', text='Rua')
    tabela.heading('Bairro', text='Bairro')
    tabela.heading('Cidade', text='Cidade')
    
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
            tabela.insert('', tk.END, values=(item['id'], item['nome'], item['contato'], item['rua'], item['bairro'], item['cidade']))

    atualizar_lista()

    frame_form = tk.Frame(scrollable_frame, bg='#ecf0f1')
    frame_form.pack(fill=tk.X, padx=15, pady=10)

    tk.Label(frame_form, text="ID:", bg='#ecf0f1', fg='#333333', font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky=tk.W, pady=5, padx=5)
    id_entry = tk.Entry(frame_form, font=('Arial', 10), bg='white', fg='#333333')
    id_entry.grid(row=0, column=1, sticky=tk.EW, pady=5, padx=5)

    tk.Label(frame_form, text="Nome:", bg='#ecf0f1', fg='#333333', font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky=tk.W, pady=5, padx=5)
    nome_entry = tk.Entry(frame_form, font=('Arial', 10), bg='white', fg='#333333')
    nome_entry.grid(row=1, column=1, sticky=tk.EW, pady=5, padx=5)

    tk.Label(frame_form, text="Contato:", bg='#ecf0f1', fg='#333333', font=('Arial', 10, 'bold')).grid(row=2, column=0, sticky=tk.W, pady=5, padx=5)
    contato_entry = tk.Entry(frame_form, font=('Arial', 10), bg='white', fg='#333333')
    contato_entry.grid(row=2, column=1, sticky=tk.EW, pady=5, padx=5)

    tk.Label(frame_form, text="Rua:", bg='#ecf0f1', fg='#333333', font=('Arial', 10, 'bold')).grid(row=3, column=0, sticky=tk.W, pady=5, padx=5)
    rua_entry = tk.Entry(frame_form, font=('Arial', 10), bg='white', fg='#333333')
    rua_entry.grid(row=3, column=1, sticky=tk.EW, pady=5, padx=5)

    tk.Label(frame_form, text="Bairro:", bg='#ecf0f1', fg='#333333', font=('Arial', 10, 'bold')).grid(row=4, column=0, sticky=tk.W, pady=5, padx=5)
    bairro_entry = tk.Entry(frame_form, font=('Arial', 10), bg='white', fg='#333333')
    bairro_entry.grid(row=4, column=1, sticky=tk.EW, pady=5, padx=5)

    tk.Label(frame_form, text="Cidade:", bg='#ecf0f1', fg='#333333', font=('Arial', 10, 'bold')).grid(row=5, column=0, sticky=tk.W, pady=5, padx=5)
    cidade_entry = tk.Entry(frame_form, font=('Arial', 10), bg='white', fg='#333333')
    cidade_entry.grid(row=5, column=1, sticky=tk.EW, pady=5, padx=5)

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
        contato_entry.delete(0, tk.END)
        contato_entry.insert(0, valores[2])
        rua_entry.delete(0, tk.END)
        rua_entry.insert(0, valores[3])
        bairro_entry.delete(0, tk.END)
        bairro_entry.insert(0, valores[4])
        cidade_entry.delete(0, tk.END)
        cidade_entry.insert(0, valores[5])

    tabela.bind('<<TreeviewSelect>>', selecionar)

    def criar():
        dados = carregar_dados()
        novo = {
            "id": id_entry.get(),
            "nome": nome_entry.get(),
            "contato": contato_entry.get(),
            "rua": rua_entry.get(),
            "bairro": bairro_entry.get(),
            "cidade": cidade_entry.get()
        }
        dados.append(novo)
        salvar_dados(dados)
        atualizar_lista()
        messagebox.showinfo("Fornecedor criado", f"Fornecedor '{novo['nome']}' (ID: {novo['id']}) criado com sucesso.")

    def atualizar():
        dados = carregar_dados()
        for item in dados:
            if item["id"] == id_entry.get():
                item.update({
                    "nome": nome_entry.get(),
                    "contato": contato_entry.get(),
                    "rua": rua_entry.get(),
                    "bairro": bairro_entry.get(),
                    "cidade": cidade_entry.get()
                })
                salvar_dados(dados)
                atualizar_lista()
                messagebox.showinfo("Fornecedor atualizado", f"Fornecedor '{item.get('nome','')}' (ID: {item.get('id','')}) atualizado com sucesso.")
                return
            messagebox.showerror("Erro - Atualizar", f"ID '{id_entry.get()}' não encontrado.")

    def deletar():
        if not messagebox.askyesno("Confirmar remoção", f"Deseja realmente deletar o fornecedor com ID '{id_entry.get()}'?"):
            return
        dados = carregar_dados()
        dados = [item for item in dados if item["id"] != id_entry.get()]
        salvar_dados(dados)
        atualizar_lista()
        messagebox.showinfo("Fornecedor deletado", f"Fornecedor com ID '{id_entry.get()}' deletado com sucesso.")

    frame_buttons = tk.Frame(scrollable_frame, bg='#ecf0f1')
    frame_buttons.pack(pady=12, expand=True)
    ttk.Button(frame_buttons, text="✅ Criar", command=criar).pack(side=tk.LEFT, padx=8)
    ttk.Button(frame_buttons, text="🔄 Atualizar", command=atualizar).pack(side=tk.LEFT, padx=8)
    ttk.Button(frame_buttons, text="🗑️ Deletar", command=deletar).pack(side=tk.LEFT, padx=8)