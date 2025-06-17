import tkinter as tk
from tkinter import font as tkfont
from usuario import carregar_usuarios, salvar_usuarios
from banco import depositar, sacar, exportar_extrato, transferir
from extrato import exportar_extrato

def atualizar_saldo_na_tela(label, novo_saldo):
    label.config(text=f"R${novo_saldo:.2f}")

def abrir_janela_transferencia(titulo, cpf, dados, label):
    janela = tk.Toplevel()
    janela.title(titulo)
    janela.geometry("300x300")
    janela.config(bg="#5e157c")

    tk.Label(janela,bg="#5e157c", fg="white", text="Valor da transferência:").pack(pady=5)
    entry_saldo = tk.Entry(janela, font=("Montserrat", 16))
    entry_saldo.pack(pady=20)

    tk.Label(janela,bg="#5e157c", fg="white", text="Cpf do destinatário:").pack(pady=5)
    entry_cpf_remetente = tk.Entry(janela, font=("Montserrat", 16))
    entry_cpf_remetente.pack(pady=20)

    def confirmar():
        try:
            valor = float(entry_saldo.get())
            if valor <= 0:
                raise ValueError
        except ValueError:
            entry_saldo.delete(0, tk.END)
            tk.messagebox.showerror("Erro", "O valor inserido é inválido")
            return
        novo_saldo = transferir(cpf, entry_cpf_remetente.get(), valor, dados)
        
        if novo_saldo == "destinatário não encontrado":
            tk.messagebox.showerror("Erro", "O destinatário não está cadastrado no sistema")
            return
        elif novo_saldo == "saldo insuficiente":
            tk.messagebox.showerror("Erro", "Transação não autorizada: Saldo insuficiente.")
            return
        elif novo_saldo == "destinatário igual remetente":
            tk.messagebox.showerror("Erro", "Transação não autorizada: Você não pode transferir para si mesmo.")
            return
        atualizar_saldo_na_tela(label, novo_saldo)
        janela.destroy()
    botao = tk.Button(janela, text="Confirmar", command=confirmar)
    botao.pack()

def abrir_janela_valor(titulo, acao, cpf, dados, label):
    janela = tk.Toplevel()
    janela.title(titulo)
    janela.geometry("300x150")
    janela.config(bg="#5e157c")

    entry = tk.Entry(janela, font=("Helvetica", 14))
    entry.pack(pady=20)

    def confirmar():
        try:
            valor = float(entry.get())
            if valor <= 0:
                raise ValueError
        except ValueError:
            entry.delete(0, tk.END)
            tk.messagebox.showerror("Erro", "O valor inserido é inválido")
            return

        if acao == "depositar":
            novo_saldo = depositar(cpf, valor, dados)
        elif acao == "sacar":
            novo_saldo = sacar(cpf, valor, dados)
            if novo_saldo is None:
                entry.delete(0, tk.END)
                tk.messagebox.showerror("Erro", "Transação não autorizada: Saldo insuficiente.")
                return     
        else:
            return

        atualizar_saldo_na_tela(label, novo_saldo)
        janela.destroy()

    botao = tk.Button(janela, text="Confirmar", command=confirmar)
    botao.pack()

def abrir_janela_principal(cpf_usuario):
    # Cria a janela principal
    root = tk.Tk()
    root.title("NatalBank")
    root.configure(bg="#5e157c")
    root.geometry("800x800")
    # Fonte personalizada
    custom_font = tkfont.Font(family="Helvetica", size=12, weight="bold")

    # Carrega dados
    dados = carregar_usuarios()
    usuario = dados[cpf_usuario]

    # Frame do saldo
    saldo_frame = tk.Frame(root, bg="#871FB4", height=150)
    saldo_frame.pack(fill="x", padx=20, pady=20)

    saldo_label = tk.Label(saldo_frame, text="Saldo disponível", 
                             bg="#871FB4", fg="white", font=custom_font,
                             anchor="w")
    saldo_label.pack(pady=(20, 5), fill="x", padx=20)


    valor_saldo = tk.Label(saldo_frame, text=f"R${usuario['saldo']:.2f}", 
                             bg="#871FB4", fg="white", font=("Helvetica", 32, "bold"),
                             anchor="w")
    

    valor_saldo.pack(pady=(0, 20), fill="x", padx=20)

    # Área principal
    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Título
    titulo_label = tk.Label(main_frame, text=f"Olá {usuario['nome']}, bem-vindo de volta!", 
                             bg="white", font=("Helvetica", 16),
                             anchor="w", justify="left")
    titulo_label.pack(pady=20, fill="x", padx=20)

    btn_frame = tk.Frame(main_frame, bg="white")
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Depositar", width=15, height=2,
              command=lambda: abrir_janela_valor("Depósito", "depositar", cpf_usuario, dados, valor_saldo)).pack(side="left", padx=10)

    tk.Button(btn_frame, text="Sacar", width=15, height=2,
              command=lambda: abrir_janela_valor("Saque", "sacar", cpf_usuario, dados, valor_saldo)).pack(side="left", padx=10)

    tk.Button(btn_frame, text="Extrato", width=15, height=2,
          command=lambda: exportar_extrato(cpf_usuario, dados)).pack(side="left", padx=10)
    
    tk.Button(btn_frame, text="Transferir", width=15, height=2,
              command=lambda: abrir_janela_transferencia("Transferência", cpf_usuario, dados, valor_saldo)).pack(side="left", padx=10)


    
    


