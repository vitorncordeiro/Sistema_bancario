import tkinter as tk
from tkinter import font as tkfont
from usuario import carregar_usuarios
from banco import depositar, sacar, transferir
from extrato import exportar_extrato


def atualizar_saldo_na_tela(label, novo_saldo):
    label.config(text=f"R${novo_saldo:.2f}")

def abrir_janela_transferencia(titulo, cpf, dados, labelSaldo):
    janela = tk.Toplevel()
    janela.title(titulo)
    janela.geometry("300x300")
    janela.config(bg="#2b2b2b")
    
    tk.Label(janela,bg="#2b2b2b", fg="white", text="Valor da transferência:").pack(pady=5)
    entry_saldo = tk.Entry(janela, font=("Montserrat", 16))
    entry_saldo.pack(pady=20)

    tk.Label(janela,bg="#2b2b2b", fg="white", text="Cpf do destinatário:").pack(pady=5)
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
        atualizar_saldo_na_tela(labelSaldo, novo_saldo)
        
        janela.destroy()
    botao = tk.Button(janela, text="Confirmar", command=confirmar)
    botao.pack()

def abrir_janela_valor(titulo, acao, cpf, dados, label):
    janela = tk.Toplevel()
    janela.title(titulo)
    janela.geometry("300x150")
    janela.config(bg="#2b2b2b")

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
    root.configure(bg="#2b2b2b")
    root.geometry("800x800")
    root.attributes("-fullscreen", True)

    # Carrega dados
    dados = carregar_usuarios()
    usuario = dados[cpf_usuario]

    # Frame do saldo
    label = criar_frame_saldo(root, f"R${usuario['saldo']:.2f}")
    # Área principal
    main_frame = tk.Frame(root, bg="#2b2b2b")
    main_frame.pack(fill="both", expand=True, padx=20, pady=10)
    
    # Título
    criar_titulo(main_frame, f"Olá {usuario['nome']}, bem-vindo de volta!")

    #Frame inferior
    frame_inferior = tk.Frame(main_frame, bg='#2b2b2b')
    frame_inferior.pack(fill=tk.BOTH, expand=True)


    #btn
    
    criar_botoes(frame_inferior, cpf_usuario, dados, label)
    
    
    
    
    
def criar_frame_saldo(framePai, texto):
    saldo_frame = tk.Frame(framePai, bg="#2b2b2b", height=150)
    saldo_frame.pack(fill="x", padx=20, pady=20)

    saldo_label = tk.Label(saldo_frame, text="Saldo disponível", 
                             bg="#2b2b2b", fg="white", font="Montserrat",
                             anchor="w")
    saldo_label.pack(pady=(20, 5), fill="x", padx=20)


    valor_saldo = tk.Label(saldo_frame, text=texto, 
                             bg="#2b2b2b", fg="white", font=("Helvetica", 32, "bold"),
                             anchor="w")
    valor_saldo.pack(pady=(0, 20), fill="x", padx=20)
    return valor_saldo
    

    

def criar_titulo(framePai, texto):
    titulo_label = tk.Label(framePai, text=texto, 
                             bg="#2b2b2b", font=("Helvetica", 30),
                             anchor="w", justify="left", fg='white')
    titulo_label.pack(pady=20, fill="x", padx=20)

def criar_botoes(framePai, cpf_usuario, dados, valor_saldo):
    btn_frame = tk.Frame(framePai, bg="#2b2b2b")
    btn_frame.pack(pady=10, side=tk.TOP)

    tk.Button(btn_frame, text="Depositar", width=15, height=2, font=("Montserrat", 20), bg="#5e157c", relief="flat", fg="white",
              command=lambda: abrir_janela_valor("Depósito", "depositar", cpf_usuario, dados, valor_saldo)).pack(side="left", padx=10)

    tk.Button(btn_frame, text="Sacar", width=15, height=2, font=("Montserrat", 20), bg="#5e157c", relief="flat", fg="white",
              command=lambda: abrir_janela_valor("Saque", "sacar", cpf_usuario, dados, valor_saldo)).pack(side="left", padx=10)

    tk.Button(btn_frame, text="Extrato", width=15, height=2, font=("Montserrat", 20), bg="#5e157c", relief="flat", fg="white",
          command=lambda: exportar_extrato(cpf_usuario, dados)).pack(side="left", padx=10)
    
    tk.Button(btn_frame, text="Transferir", width=15, height=2, font=("Montserrat", 20), bg="#5e157c", relief="flat", fg="white",
              command=lambda: abrir_janela_transferencia("Transferência", cpf_usuario, dados, valor_saldo)).pack(side="left", padx=10)
    
