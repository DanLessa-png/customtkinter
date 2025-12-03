"""
Nome do arquivo: main.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import tkinter as tk
from tkinter import ttk
from ui.ui_maquinas import MaquinasUI
from ui.ui_clientes import ClientesUI
from ui.ui_insumos import InsumosUI
from ui.ui_manutencao import ManutencaoUI
from ui.ui_fluxo_operacao import FluxoOperacaoUI

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Fazenda - Menu Principal")
        self.root.geometry("400x400")

        tk.Label(root, text="Selecione o módulo:", font=("Arial", 14)).pack(pady=20)

        tk.Button(root, text="Máquinas", width=25, command=self.abrir_maquinas).pack(pady=5)
        tk.Button(root, text="Clientes", width=25, command=self.abrir_clientes).pack(pady=5)
        tk.Button(root, text="Insumos", width=25, command=self.abrir_insumos).pack(pady=5)
        tk.Button(root, text="Manutenção", width=25, command=self.abrir_manutencao).pack(pady=5)
        tk.Button(root, text="Fluxo de Operações", width=25, command=self.abrir_fluxo_operacao).pack(pady=5)

    def abrir_maquinas(self):
        janela = tk.Toplevel(self.root)
        MaquinasUI(janela)

    def abrir_clientes(self):
        janela = tk.Toplevel(self.root)
        ClientesUI(janela)

    def abrir_insumos(self):
        janela = tk.Toplevel(self.root)
        InsumosUI(janela)

    def abrir_manutencao(self):
        janela = tk.Toplevel(self.root)
        ManutencaoUI(janela)

    def abrir_fluxo_operacao(self):
        janela = tk.Toplevel(self.root)
        FluxoOperacaoUI(janela)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
