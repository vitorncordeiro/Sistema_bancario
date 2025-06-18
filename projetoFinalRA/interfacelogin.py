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
    cadastro_window.attributes("-fullscreen", True)

    tk.Label(cadastro_window, text="Sistema de Cadastro", 
                        bg="#2B2B2B", fg="white", font=("Helvetica", 30)).pack(pady=(20, 90))
    

    tk.Label(cadastro_window, text="CPF:", bg="#2B2B2B", fg='white', font=("Montserrat", 20)).pack(pady=5)
    entry_novo_cpf = tk.Entry(cadastro_window, font=("Montserrat", 20), bg="#2B2B2B", bd=1, relief="solid", fg="#ffffff")
    entry_novo_cpf.pack()

    tk.Label(cadastro_window, text="Senha:", bg="#2B2B2B", fg='white', font=("Montserrat", 20)).pack(pady=5)
    entry_nova_senha = tk.Entry(cadastro_window, show="*", font=("Montserrat", 20), bg="#2B2B2B", bd=1, relief="solid", fg="#ffffff")
    entry_nova_senha.pack()

    tk.Label(cadastro_window, text="Primeiro Nome:", bg="#2B2B2B", fg='white', font=("Montserrat", 20)).pack(pady=5)
    entry_primeiro_nome = tk.Entry(cadastro_window, font=("Montserrat", 20), bg="#2B2B2B", bd=1, relief="solid", fg="#ffffff")
    entry_primeiro_nome.pack()

    tk.Label(cadastro_window, text="Sobrenome:", bg="#2B2B2B", fg='white', font=("Montserrat", 20)).pack(pady=5)
    entry_sobrenome = tk.Entry(cadastro_window, font=("Montserrat", 20), bg="#2B2B2B", bd=1, relief="solid", fg="#ffffff")
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

    tk.Button(cadastro_window,bg="#871Fb4", text="Cadastrar", command=cadastrar, fg="white", relief="flat",
          font=("Montserrat", 18), width=10).pack(pady=20)

janela_login = tk.Tk()
janela_login.title("NatalBank - Login")
janela_login.geometry("800x800")
janela_login.configure(bg="#2B2B2B")
janela_login.attributes("-fullscreen", True)

titulo_label = tk.Label(janela_login, text="Sistema de Login", 
                        bg="#2B2B2B", fg="white", font=("Helvetica", 30))
titulo_label.pack(pady=(20, 5), fill="x", padx=20)

frame_central = tk.Frame(janela_login, bg="#2B2B2B")
frame_central.pack(expand=True, pady=(0, 200))

# Widgets dentro do frame central


tk.Label(frame_central, text="CPF:", bg="#2B2B2B", fg='white', font=("Montserrat", 20)).pack(pady=5)
entry_cpf = tk.Entry(frame_central, font=("Montserrat", 20), bg="#2B2B2B", bd=1, relief="solid", fg="#ffffff")
entry_cpf.pack()

tk.Label(frame_central, text="Senha:", bg="#2b2b2b", fg='white', font=("Montserrat", 20)).pack(pady=5)
entry_senha = tk.Entry(frame_central, show="*", font=("Montserrat", 20), bg="#2B2B2B", bd=1, relief="solid", fg="#ffffff")
entry_senha.pack()

tk.Button(frame_central, text="Entrar", command=tentar_login, fg="white", bg="#871FB4", relief="flat",
          font=("Montserrat", 18), width=10).pack(pady=(50, 0))

tk.Button(frame_central, text="Cadastrar", command=abrir_janela_cadastro, fg="white", bg="#871FB4", relief="flat",
          font=("Montserrat", 18), width=10).pack(pady=20)
