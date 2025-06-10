import tkinter as tk
from tkinter import font as tkfont

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Natalbank")
        self.root.geometry("1000x700")
        self.root.configure(bg="#5e147c")
        
        # Fonte personalizada
        self.custom_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Cabeçalho
        self.header_frame = tk.Frame(self.root, bg="#5e147c", height=80)
        self.header_frame.pack(fill="x", padx=20, pady=(20, 10))
        
        self.menu_button = tk.Button(self.header_frame, text="☰", bg="#5e147c", fg="white", 
                                   borderwidth=0, font=self.custom_font)
        self.menu_button.pack(side="left")
        
        
        # Saldo
        self.balance_frame = tk.Frame(self.root, bg="#5e147c", height=150)
        self.balance_frame.pack(fill="x", padx=20, pady=10)
        
        
       
        #area princpal
        
        self.main_frame = tk.Frame(self.root, bg="#171718")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20, anchor='w')
        
        self.balance_label = tk.Label(self.main_frame, text="Saldo em conta", 
                                     bg="#171718", fg="white", font=self.custom_font, anchor="w")
        self.balance_label.pack(pady=(20, 5))
        
        self.balance_value = tk.Label(self.main_frame, text="R$ 5000,00", 
                                     bg="#171718", fg="white", font=("Helvetica", 32, "bold"), anchor="w")
        self.balance_value.pack(pady=(0, 20))
        self.welcome_label = tk.Label(self.main_frame, text="Olá, bem-vindo de volta!", 
                                    bg="#171718",fg="white", font=("Helvetica", 16), anchor="w")
        self.welcome_label.pack(pady=20)
        
        # Atalhos rápidos
        shortcuts = ["Pagar conta", "Transferir", "Depositar", "Recarga"]
        self.shortcuts_frame = tk.Frame(self.main_frame, bg="#171718")
        self.shortcuts_frame.pack()
        
        for i, shortcut in enumerate(shortcuts):
            btn = tk.Button(self.shortcuts_frame, text=shortcut, bg="#272727", fg="white", 
                          borderwidth=0, font=self.custom_font, width=15, height=3)
            btn.grid(row=0, column=i, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()
