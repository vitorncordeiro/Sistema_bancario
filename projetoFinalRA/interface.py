import tkinter as tk
from tkinter import font as tkfont


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Nubank Simples")
        self.root.configure(bg="#5e157c")
        
        self.custom_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Cabeçalho
        self.header_frame = tk.Frame(self.root, bg="#5e157c", height=80)
        self.header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        self.menu_button = tk.Button(self.header_frame, text="☰", bg="#5e157c", fg="white", 
                                   borderwidth=0, font=self.custom_font)
        self.menu_button.pack(side="left")
        
        
        # Saldo (agora alinhado à esquerda)
        self.balance_frame = tk.Frame(self.root, bg="#871FB4", height=150)
        self.balance_frame.pack(fill="x", padx=20, pady=10)
        
        self.balance_label = tk.Label(self.balance_frame, text="Saldo disponível", 
                                     bg="#871FB4", fg="white", font=self.custom_font,
                                     anchor="w")
        self.balance_label.pack(pady=(20, 5), fill="x", padx=20)
        
        self.balance_value = tk.Label(self.balance_frame, text="R$ 5.000,00", 
                                     bg="#871FB4", fg="white", font=("Helvetica", 32, "bold"),
                                     anchor="w")
        self.balance_value.pack(pady=(0, 20), fill="x", padx=20)
        
        # Área principal
        self.main_frame = tk.Frame(self.root, bg="white")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Mensagem de boas-vindas alinhada à esquerda
        self.welcome_label = tk.Label(self.main_frame, text="Olá, bem-vindo de volta!", 
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

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
