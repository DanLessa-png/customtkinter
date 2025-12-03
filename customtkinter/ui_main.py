

import customtkinter as ctk
from ui.ui_maquinas import MaquinasUI
from ui.ui_clientes import ClientesUI
from ui.ui_insumos import InsumosUI
from ui.ui_manutencao import ManutencaoUI
from ui.ui_fluxo_operacao import OperacaoUI

class MainUI(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)

        title = ctk.CTkLabel(self, text="Sistema de Gestão Agrícola", font=("Arial", 28, "bold"))
        title.pack(pady=20)

        btns = [
            ("Gerenciar Máquinas", MaquinasUI),
            ("Clientes & Cooperativas", ClientesUI),
            ("Estoque de Insumos", InsumosUI),
            ("Manutenções", ManutencaoUI),
            ("Operações no Campo", OperacaoUI),
        ]

        for texto, janela in btns:
            ctk.CTkButton(
                self,
                text=texto,
                width=280,
                height=50,
                corner_radius=15,
                command=lambda j=janela: j(master)
            ).pack(pady=10)
