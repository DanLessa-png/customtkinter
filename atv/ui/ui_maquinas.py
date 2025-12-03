import customtkinter as ctk
from modules.maquinas import MaquinasDB

class MaquinasUI(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Cadastro de Máquinas Agrícolas")
        self.geometry("600x500")
        self.resizable(False, False)

        ctk.CTkLabel(self, text="Máquinas Agrícolas", font=("Arial", 24, "bold")).pack(pady=20)

        self.tipo = ctk.CTkEntry(self, placeholder_text="Tipo (Trator, Colheitadeira...)")
        self.modelo = ctk.CTkEntry(self, placeholder_text="Modelo")
        self.ano = ctk.CTkEntry(self, placeholder_text="Ano")
        self.horimetro = ctk.CTkEntry(self, placeholder_text="Horímetro")
        self.status = ctk.CTkEntry(self, placeholder_text="Status (Ativa, Manutenção...)")

        widgets = [self.tipo, self.modelo, self.ano, self.horimetro, self.status]
        for w in widgets:
            w.pack(pady=10, fill="x", padx=40)

        ctk.CTkButton(self, text="Salvar Máquina", command=self.salvar).pack(pady=20)

    def salvar(self):
        dados = [
            self.tipo.get(),
            self.modelo.get(),
            self.ano.get(),
            self.horimetro.get(),
            self.status.get()
        ]
        MaquinasDB.salvar(dados)
        self.destroy()
