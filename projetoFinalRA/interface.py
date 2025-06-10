import tkinter as tk
from tkinter import font as tkfont
from usuario import carregar_usuarios, salvar_usuarios

class MainApp:
    def __init__(self, root, cpf_usuario):
        self.root = root
        self.root.title("NatalBank")
        self.root.configure(bg="#5e157c")
        self.cpf = cpf_usuario  # salva o CPF

        self.custom_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
        
        self.dados = carregar_usuarios()
        self.usuario = self.dados[self.cpf]
        self.create_widgets()
    def create_widgets(self):
        # Cabeçalho
        
        
        
        # Saldo (agora alinhado à esquerda)
        self.balance_frame = tk.Frame(self.root, bg="#871FB4", height=150)
        self.balance_frame.pack(fill="x", padx=20, pady=20)
        
        self.balance_label = tk.Label(self.balance_frame, text="Saldo disponível", 
                                     bg="#871FB4", fg="white", font=self.custom_font,
                                     anchor="w")
        self.balance_label.pack(pady=(20, 5), fill="x", padx=20)
        
        self.balance_value = tk.Label(self.balance_frame, text=f"R${self.usuario['saldo']}", 
                                     bg="#871FB4", fg="white", font=("Helvetica", 32, "bold"),
                                     anchor="w")
        self.balance_value.pack(pady=(0, 20), fill="x", padx=20)
        
        # Área principal
        self.main_frame = tk.Frame(self.root, bg="white")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Mensagem de boas-vindas alinhada à esquerda
        self.welcome_label = tk.Label(self.main_frame, text=f"Olá {self.usuario['nome']}, bem-vindo de volta!", 
                                    bg="white", font=("Helvetica", 16),
                                    anchor="w", justify="left")
        self.welcome_label.pack(pady=20, fill="x", padx=20)
        
        # Atalhos rápidos
        shortcuts = ["Depositar", "Sacar", "Caixinha", "Exportar extrato"]
        self.shortcuts_frame = tk.Frame(self.main_frame, bg="white")
        self.shortcuts_frame.pack()
        
        for i, shortcut in enumerate(shortcuts):
            btn = tk.Button(self.shortcuts_frame, text=shortcut, bg="#f5f5f5", fg="#333", 
                          borderwidth=0, font=self.custom_font, width=15, height=3)
            btn.grid(row=0, column=i, padx=10, pady=10)

def abrir_janela_principal(cpf_usuario):
    root = tk.Tk()
    app = MainApp(root, cpf_usuario)
    root.mainloop()

