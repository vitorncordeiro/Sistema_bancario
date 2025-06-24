import tkinter as tk
from tkinter import messagebox
from usuario import carregar_usuarios
from banco import depositar, sacar, transferir
from extrato import exportar_extrato

def atualizar_saldo_na_tela(label, novo_saldo):
    label.config(text=f"R${novo_saldo:.2f}")

def abrir_janela_transferencia(titulo, cpf, dados, label):
    janela = tk.Toplevel()
    janela.title(titulo)
    janela.geometry("300x300")
    janela.config(bg="#2b2b2b")

    tk.Label(janela, bg="#2b2b2b", fg="white", text="Valor da transferência:").pack(pady=5)
    entry_saldo = tk.Entry(janela, font=("Montserrat", 16))
    entry_saldo.pack(pady=20)

    tk.Label(janela, bg="#2b2b2b", fg="white", text="Cpf do destinatário:").pack(pady=5)
    entry_cpf_destinatario = tk.Entry(janela, font=("Montserrat", 16))
    entry_cpf_destinatario.pack(pady=20)

    def confirmar():
        try:
            valor = float(entry_saldo.get())
            if valor <= 0:
                raise ValueError
        except ValueError:
            entry_saldo.delete(0, tk.END)
            messagebox.showerror("Erro", "O valor inserido é inválido")
            janela.destroy()
            return

        novo_saldo = transferir(cpf, entry_cpf_destinatario.get(), valor, dados)

        if novo_saldo == "destinatário não encontrado":
            messagebox.showerror("Erro", "O destinatário não está cadastrado no sistema")
            janela.destroy()
            return
        elif novo_saldo == "saldo insuficiente":
            messagebox.showerror("Erro", "Transação não autorizada: Saldo insuficiente.")
            janela.destroy()
            return
        elif novo_saldo == "destinatário igual remetente":
            messagebox.showerror("Erro", "Transação não autorizada: Você não pode transferir para si mesmo.")
            janela.destroy()
            return

        atualizar_saldo_na_tela(label, novo_saldo)
        janela.destroy()

    tk.Button(janela, text="Confirmar", command=confirmar).pack()

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
            messagebox.showerror("Erro", "O valor inserido é inválido")
            janela.destroy()
            return

        if acao == "depositar":
            novo_saldo = depositar(cpf, valor, dados)
        elif acao == "sacar":
            novo_saldo = sacar(cpf, valor, dados)
            if novo_saldo is None:
                entry.delete(0, tk.END)
                messagebox.showerror("Erro", "Transação não autorizada: Saldo insuficiente.")
                janela.destroy()
                return
        else:
            return

        atualizar_saldo_na_tela(label, novo_saldo)
        janela.destroy()

    tk.Button(janela, text="Confirmar", command=confirmar).pack()

def criar_frame_saldo(framePai, texto):
    saldo_frame = tk.Frame(framePai, bg="#2b2b2b", height=150)
    saldo_frame.pack(fill="x", padx=20, pady=20)

    tk.Label(saldo_frame, text="Saldo disponível", bg="#2b2b2b", fg="white", font="Montserrat", anchor="w").pack(pady=(20, 5), fill="x", padx=20)

    valor_saldo = tk.Label(saldo_frame, text=texto, bg="#2b2b2b", fg="white", font=("Helvetica", 32, "bold"), anchor="w")
    valor_saldo.pack(pady=(0, 20), fill="x", padx=20)
    return valor_saldo

def criar_titulo(framePai, texto):
    tk.Label(framePai, text=texto, bg="#2b2b2b", font=("Helvetica", 16), anchor="w", justify="left", fg='white').pack(pady=20, fill="x", padx=20)

def mostrar_historico(framePai, cpf_usuario, dados):
    tk.Label(framePai, text="   Últimas transações", bg="#2B2B2B", fg="white", font=("Arial", 16)).pack(anchor="w", padx=10, pady=4)
    transacoes = dados[cpf_usuario].get("transacoes", [])
    ultimas_5 = transacoes[-5:][::-1]
    for transacao in ultimas_5:
        tipo = transacao["tipo"]
        valor = transacao["valor"]
        data = transacao["data_hora"]
        texto = f" {tipo.capitalize()} \n{data} \nR$ {valor:.2f}"
        tk.Label(framePai, text=texto, bg="#2B2B2B", fg="white", font=("Arial", 14)).pack(anchor="w", padx=10, pady=2)

def criar_botoes(framePai, cpf_usuario, dados, label, atualizar_historico):
    btn_frame = tk.Frame(framePai, bg="#2b2b2b")
    btn_frame.pack(pady=10, side="top")

    tk.Button(btn_frame, text="Depositar", width=15, height=2, font=("Montserrat", 20), bg="#5e157c", relief="flat", fg="white",
              command=lambda: abrir_janela_valor("Depósito", "depositar", cpf_usuario, dados, label)).pack(side="left", padx=10)

    tk.Button(btn_frame, text="Sacar", width=15, height=2, font=("Montserrat", 20), bg="#5e157c", relief="flat", fg="white",
              command=lambda: abrir_janela_valor("Saque", "sacar", cpf_usuario, dados, label)).pack(side="left", padx=10)

    tk.Button(btn_frame, text="Transferir", width=15, height=2, font=("Montserrat", 20), bg="#5e157c", relief="flat", fg="white",
              command=lambda: abrir_janela_transferencia("Transferência", cpf_usuario, dados, label)).pack(side="left", padx=10)
    tk.Button(btn_frame, text="Extrato", width=15, height=2, font=("Montserrat", 20), bg="#5e157c", relief="flat", fg="white",
              command=lambda: exportar_extrato(cpf_usuario, dados)).pack(side="left", padx=10)
    tk.Button(btn_frame, text="Atualizar Histórico", width=15, height=2, font=("Montserrat", 20), bg="#5e157c", relief="flat", fg="white",
              command=atualizar_historico).pack(side="left", padx=10)

def abrir_janela_principal(cpf_usuario):
    root = tk.Tk()
    root.title("NatalBank")
    root.configure(bg="#2b2b2b")
    root.geometry("800x800")
    root.attributes("-fullscreen", True)

    dados = carregar_usuarios()
    usuario = dados[cpf_usuario]

    label = criar_frame_saldo(root, f"R${usuario['saldo']:.2f}")
    main_frame = tk.Frame(root, bg="#2b2b2b")
    main_frame.pack(fill="both", expand=True, padx=20, pady=10)

    criar_titulo(main_frame, f"Olá {usuario['nome']}, bem-vindo de volta!")

    frame_inferior = tk.Frame(main_frame, bg='#2b2b2b')
    frame_inferior.pack(expand=True, side="top")

    frame_historico = tk.Frame(frame_inferior, bg='#2b2b2b')
    frame_historico.pack(pady=20)

    mostrar_historico(frame_historico, cpf_usuario, dados)

    def atualizar_historico():
        for widget in frame_historico.winfo_children():
            widget.destroy()
        mostrar_historico(frame_historico, cpf_usuario, dados)

    criar_botoes(frame_inferior, cpf_usuario, dados, label, atualizar_historico)

    