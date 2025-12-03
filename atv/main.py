"""
Nome do arquivo: main.py
Equipe: João, José, Maria e Pedro.
Turma: G93311
Semestre: 2025.2
"""

import customtkinter as ctk
from ui_main import MainUI

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestão Agrícola - AgroManager")
        self.geometry("900x600")
        self.resizable(False, False)

        MainUI(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()
