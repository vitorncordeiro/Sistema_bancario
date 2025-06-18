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



def transferir(cpfRemetente, cpfDestinatario, valor, dados):
    if valor > dados[cpfRemetente]["saldo"]:
        return "saldo insuficiente"
        
    elif cpfRemetente == cpfDestinatario:
        return "destinário igual remetente"
    try:
        dados[cpfRemetente]["saldo"] -= valor
        dados[cpfDestinatario]["saldo"] += valor
        registrar_transacao(cpfRemetente, f"transferência para {cpfDestinatario}", valor, dados)
        registrar_transacao(cpfDestinatario, f"transferência de   {cpfRemetente}  ", valor, dados)
        salvar_usuarios(dados)
        return dados[cpfRemetente]["saldo"]
    
    except KeyError:
        return "destinatário não encontrado"




# Mapeamento dos nomes para funções