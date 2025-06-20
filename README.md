# Sistema Bancário (Projeto Final - Raciocínio Algorítmico)

Este repositório contém um **protótipo de sistema bancário** desenvolvido como **projeto final da disciplina de Raciocínio Algorítmico**, cursada no **primeiro período de Engenharia de Software**. O projeto foi orientado pelo professor **Maicris Fernandes** e tem como objetivo aplicar os fundamentos de lógica computacional, estruturas de decisão, funções e manipulação de dados.

## 💻 Tecnologias utilizadas

* **Python 3**
* **Tkinter** (interface gráfica)
* Manipulação de arquivos `.txt` para persistência de dados

## 📌 Funcionalidades

O sistema permite ao usuário:

* **Cadastrar e logar com CPF**
* **Consultar saldo**
* **Depositar, sacar e transferir valores**
* **Visualizar extrato bancário**
* **Exportar extrato para arquivo `.txt`**

## 🗂️ Estrutura do Projeto

```
Sistema_bancario/
│
├── banco.py               # Funções principais do sistema bancário
├── caixinha.py            # Gerenciamento da funcionalidade de caixinha
├── extrato.py             # Controle de extratos e exportações
├── graficos.py            # Geração de gráficos com Matplotlib
├── interface.py           # Interface gráfica principal com Tkinter
├── usuario.py             # Cadastro e autenticação de usuários
└── dados/                 # Pasta onde os dados são armazenados (.txt)
```

## ▶️ Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/vitorncordeiro/Sistema_bancario.git
   cd Sistema_bancario
   ```

2. Execute o arquivo `main.py`:

   ```bash
   python main.py
   ```

> **Requisitos:** Certifique-se de ter o Python 3 instalado com o pacote `tkinter`.

## 👨‍💻 Autor

**Vitor Cordeiro**
Aluno de Engenharia de Software - 1º período

---

