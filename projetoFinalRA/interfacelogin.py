from usuario import fazer_login, cadastrar_usuario, inicializar_arquivo
from interface import abrir_janela_principal
import tkinter as tk
from tkinter import messagebox

def tentar_login():
    cpf = entry_cpf.get()
    senha = entry_senha.get()

    if fazer_login(cpf, senha):
        messagebox.showinfo("Login", "Login bem-sucedido!")
        janela_login.destroy()
        abrir_janela_principal(cpf)
    else:
        messagebox.showerror("Erro", "CPF ou senha inválidos.")

def abrir_janela_cadastro():
    cadastro_window = tk.Toplevel()
    cadastro_window.title("Natalbank - Cadastrar Usuário")
    cadastro_window.geometry("500x300")
    cadastro_window.config(bg="#5e157c")
    tk.Label(cadastro_window,bg="#5e157c", fg="white", text="CPF:").pack(pady=5)
    entry_novo_cpf = tk.Entry(cadastro_window)
    entry_novo_cpf.pack()

    tk.Label(cadastro_window,bg="#5e157c", fg="white", text="Senha:").pack(pady=5)
    entry_nova_senha = tk.Entry(cadastro_window, show="*")
    entry_nova_senha.pack()

    tk.Label(cadastro_window, bg="#5e157c", fg="white", text="Primeiro Nome").pack(pady=5)
    entry_primeiro_nome = tk.Entry(cadastro_window)
    entry_primeiro_nome.pack()

    tk.Label(cadastro_window, bg="#5e157c", fg="white", text="Sobrenome").pack(pady=5)
    entry_sobrenome = tk.Entry(cadastro_window)
    entry_sobrenome.pack()


    def cadastrar():
        cpf = entry_novo_cpf.get()
        senha = entry_nova_senha.get()
        primeiro_nome = entry_primeiro_nome.get()
        sobrenome = entry_sobrenome.get()
        cadastro = cadastrar_usuario(cpf, senha, primeiro_nome, sobrenome)
        if cadastro == 'cadastrado':
            messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
            cadastro_window.destroy()
        elif cadastro == 'cpf existente':
            messagebox.showerror("Erro", "CPF já cadastrado")
        elif cadastro == 'cpf invalido':
            messagebox.showerror("Erro", "CPF inválido")
        elif cadastro == 'dados incompletos':
            messagebox.showerror("Erro", "Preencha todos os campos")

    tk.Button(cadastro_window,bg="#871Fb4",relief="flat", fg="white", text="Cadastrar", command=cadastrar).pack(pady=20)

janela_login = tk.Tk()
janela_login.title("NatalBank - Login")
janela_login.geometry("500x300")
janela_login.configure(bg="#5e157c")
titulo_label = tk.Label(janela_login, text="Já possui uma conta? Insira suas credenciais", 
                                     bg="#871FB4", fg="white", font="Helvetica"
                                     )
titulo_label.pack(pady=(20, 5), fill="x", padx=20)

tk.Label(janela_login, text="CPF:", bg="#5e157c", fg='white').pack(pady=5)
entry_cpf = tk.Entry(janela_login)
entry_cpf.pack()

tk.Label(janela_login, text="Senha:", bg="#5e157c", fg='white').pack(pady=5)
entry_senha = tk.Entry(janela_login, show="*")
entry_senha.pack()

tk.Button(janela_login, text="Entrar", command=tentar_login, fg="white", bg="#871FB4", relief="flat").pack(pady=10)
tk.Button(janela_login, text="Cadastrar", command=abrir_janela_cadastro, fg="white", bg="#871FB4", relief="flat").pack(pady=5)
