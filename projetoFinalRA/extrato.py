import os
from datetime import datetime
from tkinter import messagebox

def exportar_extrato(cpf, dados):
    usuario = dados.get(cpf)
    if not usuario:
        raise ValueError("Usuário não encontrado.")

    nome_completo = f"{usuario['nome']} {usuario['sobrenome']}"
    transacoes = usuario.get("transacoes", [])
    saldo = usuario.get("saldo", 0.0)

    

    # Criação da pasta se não existir
    os.makedirs("extratos", exist_ok=True)
    caminho_arquivo = os.path.join("extratos", f"extrato_{cpf}.txt")

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write("="*65 + "\n")
        f.write("                        EXTRATO BANCÁRIO\n")
        f.write("="*65 + "\n\n")
        f.write(f"Nome: {nome_completo}\n")
        f.write(f"CPF: {cpf}\n")
        f.write(f"Data de emissão: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write("\n" + "-"*65 + "\n")
        f.write("        DATA        |   TIPO                         |  VALOR \n")
        f.write("-"*65 + "\n")

        for transacao in transacoes:
            data = transacao["data_hora"]
            tipo = transacao["tipo"].capitalize()
            if tipo == "Saque":
                tipo = tipo + " "*25
            elif tipo == "Deposito":
                tipo = tipo + " "*22
            valor = f"{transacao['valor']:.2f}"
            f.write(f"{data} | {tipo:<7} | {valor:>10}\n")

        f.write("-"*65 + "\n")
        f.write(f"Saldo final: R${saldo:.2f}\n")
        f.write("="*65 + "\n")
        os.startfile(caminho_arquivo)
    return caminho_arquivo
