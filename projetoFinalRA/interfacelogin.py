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
    cadastro_window.geometry("800x800")
    cadastro_window.config(bg="#2B2B2B")

    

    tk.Label(cadastro_window,bg="#2B2B2B", fg="white", text="CPF:").pack(pady=5)
    entry_novo_cpf = tk.Entry(cadastro_window)
    entry_novo_cpf.pack()

    tk.Label(cadastro_window,bg="#2B2B2B", fg="white", text="Senha:").pack(pady=5)
    entry_nova_senha = tk.Entry(cadastro_window, show="*")
    entry_nova_senha.pack()

    tk.Label(cadastro_window, bg="#2B2B2B", fg="white", text="Primeiro Nome").pack(pady=5)
    entry_primeiro_nome = tk.Entry(cadastro_window)
    entry_primeiro_nome.pack()

    tk.Label(cadastro_window, bg="#2B2B2B", fg="white", text="Sobrenome").pack(pady=5)
    entry_sobrenome = tk.Entry(cadastro_window)
    entry_sobrenome.pack()

    
    def cadastrar():
        """Essa função deve ser interna da abrir_janela_cadastro pois modifica a janela do cadastro"""
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
janela_login.geometry("800x800")
janela_login.configure(bg="#2B2B2B")
titulo_label = tk.Label(janela_login, text="Sistema de Login", 
                                     bg="#2B2B2B", fg="white", font=("Helvetica", 30)
                                     )
titulo_label.pack(pady=(20, 5), fill="x", padx=20)

tk.Label(janela_login, text="CPF:", bg="#2B2B2B", fg='white', font=("Montserrat", 20)).pack(pady=5)
entry_cpf = tk.Entry(janela_login, font=("Montserrat", 20), bg="#2B2B2B", bd=1, relief="solid", fg="#ffffff")
entry_cpf.pack()

tk.Label(janela_login, text="Senha:", bg="#2B2B2B", fg='white', font=("Montserrat", 20)).pack(pady=5)
entry_senha = tk.Entry(janela_login, show="*", font=("Montserrat", 20), bg="#2B2B2B", bd=2, relief="solid", fg="#ffffff")
entry_senha.pack()

tk.Button(janela_login, text="Entrar", command=tentar_login, fg="white", bg="#871FB4", relief="flat",font=("Montserrat", 18), width=10).pack(pady=10)
tk.Button(janela_login, text="Cadastrar", command=abrir_janela_cadastro, fg="white", bg="#871FB4", relief="flat", font=("Montserrat", 18), width=10).pack(pady=5)
