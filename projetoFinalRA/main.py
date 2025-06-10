from usuario import fazer_login, cadastrar_usuario, inicializar_arquivo
from interface import abrir_janela_principal
from interfacelogin import tentar_login, abrir_janela_cadastro, janela_login
import tkinter as tk
from tkinter import messagebox


# Inicializa o JSON
inicializar_arquivo()

# Janela de login

janela_login.mainloop()
