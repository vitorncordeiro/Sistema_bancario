import json
import os
from validadorCpf import validar_cpf
CAMINHO_ARQUIVO = os.path.join("data", "_dados.json")


def inicializar_arquivo():
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
            json.dump({}, f)

def carregar_usuarios():
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)



def salvar_usuarios(usuarios):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4)

def cadastrar_usuario(cpf, senha, primeiroNome, sobrenome):
    dados = carregar_usuarios()
    isCpf_valido = validar_cpf(cpf)
    if cpf in dados:
        return "cpf existente"  # já existe
    
    if isCpf_valido == False:
        return "cpf invalido"
    elif validar_cadastro(cpf, senha, primeiroNome, sobrenome):
        dados[cpf] = {
            "nome": primeiroNome,
            "sobrenome": sobrenome,
            "senha": senha,
            "saldo": 0.0,
            "transacoes": [],
            "caixinhas": {}  # nenhuma criada por padrão
        }
        salvar_usuarios(dados)
        return 'cadastrado'
    else:
        return 'dados incompletos'
    
def validar_cadastro(cpf, senha, primeiroNome, sobrenome):
    
    if senha and primeiroNome and sobrenome and cpf:
        return True
    else:
        return False

def fazer_login(cpf, senha):
    usuarios = carregar_usuarios()
    if cpf in usuarios and usuarios[cpf]["senha"] == senha:
        print("Login bem-sucedido!")
        return True
    else:
        print("CPF ou senha inválidos.")
        return False

# Inicializa o arquivo se necessário
inicializar_arquivo()
