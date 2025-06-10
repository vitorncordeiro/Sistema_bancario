from pathlib import Path
import json
caminho_db = Path(__file__).parent / "db.json"

with open(caminho_db, 'w+') as arquivo:
    dictJson = json.load(arquivo)

class User:
    def __init__(self, nome):
        self.nome = nome
    def criar_usuario(self, cpf, senha):
        self.senha = senha
        self.cpf = cpf
        dictJson[cpf] = senha
    def logar(self):
        senhaI = input('Digite sua senha: ')
        cpfI = input('Digite seu cpf: ')
        if senhaI == dictJson[cpfI]:
            print('Logou')
        else:

            print('Erro')

user1 = User("Vitor")
user1.criar_usuario("123456789", "senha123")
user1.logar("123456789", "senha123")
