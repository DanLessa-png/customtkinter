"""
Nome do arquivo: main.py
Equipe: Dan Lessa e Kevin Anjos
Turma: G93311
Semestre: 2025.2
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import window_manager
import pecas
import fornecedores
import maquinas
import funcionarios
import clientes
import saidas


def abrir_crud_pecas():
    pecas.abrir_janela()

def abrir_crud_fornecedores():
    fornecedores.abrir_janela()

def abrir_crud_maquinas():
    maquinas.abrir_janela()

def abrir_crud_funcionarios():
    funcionarios.abrir_janela()

def abrir_crud_clientes():
    clientes.abrir_janela()

def abrir_crud_saidas():
    saidas.abrir_janela()


raiz = tk.Tk()
raiz.title("AgroManager - Sistema de Gerenciamento de Máquinas Agrícolas")
raiz.geometry("1024x768")
raiz.configure(bg='#ecf0f1')

estilo = ttk.Style(raiz)
try:
    estilo.theme_use('clam')
except Exception:
    pass
estilo.configure('Acento.TButton', background='#1a5f7a', foreground='white', padding=10, font=('Arial', 10, 'bold'))
estilo.configure('Secundario.TButton', background='#2ecc71', foreground='white', padding=8, font=('Arial', 10))

cabecalho = ttk.Label(raiz, text="🏭 AgroManager", font=("Arial", 32, "bold"), background='#ecf0f1', foreground='#1a5f7a')
cabecalho.pack(pady=20)

subtitulo = ttk.Label(raiz, text="Sistema de Gerenciamento de Máquinas Agrícolas", font=("Arial", 10), background='#ecf0f1', foreground='#555555')
subtitulo.pack(pady=5)

painel_botoes = ttk.Frame(raiz)
painel_botoes.pack(padx=40, pady=10, fill=tk.X)

ttk.Button(painel_botoes, text="⚙️  Gerenciar Peças/Insumos", command=abrir_crud_pecas, style='Acento.TButton').pack(fill=tk.X, pady=6)
ttk.Button(painel_botoes, text="🚚 Gerenciar Fornecedores", command=abrir_crud_fornecedores, style='Acento.TButton').pack(fill=tk.X, pady=6)
ttk.Button(painel_botoes, text="🚜 Gerenciar Máquinas Agrícolas", command=abrir_crud_maquinas, style='Acento.TButton').pack(fill=tk.X, pady=6)
ttk.Button(painel_botoes, text="👥 Gerenciar Funcionários", command=abrir_crud_funcionarios, style='Acento.TButton').pack(fill=tk.X, pady=6)
ttk.Button(painel_botoes, text="🏢 Gerenciar Clientes", command=abrir_crud_clientes, style='Acento.TButton').pack(fill=tk.X, pady=6)
ttk.Button(painel_botoes, text="📤 Gerenciar Saídas", command=abrir_crud_saidas, style='Acento.TButton').pack(fill=tk.X, pady=6)


def sair_tela_cheia(event=None):
    raiz.attributes('-fullscreen', False)

raiz.bind('<Escape>', sair_tela_cheia)


ttk.Button(raiz, text="❌ Sair", command=raiz.destroy, style='Secundario.TButton').pack(side=tk.BOTTOM, pady=10)


def alternar_tela_cheia():
    cur = raiz.attributes('-fullscreen')
    if cur:
        raiz.attributes('-fullscreen', False)
        raiz.geometry('1024x768')
    else:
        raiz.attributes('-fullscreen', True)

ttk.Button(raiz, text="🔲 Alternar Tela Cheia", command=alternar_tela_cheia, style='Secundario.TButton').pack(side=tk.BOTTOM, pady=6)

raiz.mainloop()