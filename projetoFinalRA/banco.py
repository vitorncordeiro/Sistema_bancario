from usuario import carregar_usuarios, salvar_usuarios
from datetime import datetime

def registrar_transacao(cpf, tipo, valor, dados):
    transacao = {
        "tipo": tipo,
        "valor": round(valor, 2),
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    dados[cpf]["transacoes"].append(transacao)

def depositar(cpf, valor, dados):
    
    dados[cpf]["saldo"] += valor
    registrar_transacao(cpf, "deposito", valor, dados)
    salvar_usuarios(dados)
    return dados[cpf]["saldo"]

def sacar(cpf, valor, dados):
    if valor > dados[cpf]["saldo"]:
        return None  # saldo insuficiente
    dados[cpf]["saldo"] -= valor
    registrar_transacao(cpf, "saque", valor, dados)
    salvar_usuarios(dados)
    return dados[cpf]["saldo"]

def caixinha(cpf, nomeDaCaixinha):
    print("Função: Caixinha")

def exportar_extrato():
    print("Função: Exportar extrato")

# Mapeamento dos nomes para funções
funcoes_botoes = {
    "Depositar": depositar,
    "Sacar": sacar,
    "Caixinha": caixinha,
    "Exportar extrato": exportar_extrato
}
