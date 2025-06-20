# 🏦 Sistema Bancário

Projeto final da disciplina de **Raciocínio Algorítmico**, do curso de Engenharia de Software, ministrada pelo professor **Maicris Fernandes**.

---

## 🎯 Objetivo

Desenvolver um sistema bancário simples em Java, com foco em lógica algorítmica, estruturas de controle, manipulação de dados e tratamento de exceções, que:

- **Gerencia contas** (abrir, consultar, depositar, sacar, encerrar).
- **Valida entradas** do usuário com tratamento de erros.
- Demonstra uso de **orientação a objetos** e boas práticas de codificação.

---

## 📁 Estrutura do projeto

```

Sistema\_bancario/
├── src/
│   ├── Main.java
│   ├── Banco.java
│   ├── Conta.java
│   ├── Cliente.java
│   └── Utils.java
└── README.md

````

- `Main.java`: ponto de entrada do sistema com menu interativo.
- `Banco.java`: gerencia a lista de contas e operações bancárias.
- `Conta.java`: representa uma conta bancária (número, titular, saldo).
- `Cliente.java`: estrutura de dados do cliente (nome, CPF, etc.).
- `Utils.java`: métodos auxiliares (validação de input, leituras via `Scanner`).

---

## ⚙️ Como executar

1. Clone o projeto:
   ```bash
   git clone https://github.com/vitorncordeiro/Sistema_bancario.git
````

2. Entre na pasta principal:

   ```bash
   cd Sistema_bancario
   ```
3. Compile todos os arquivos:

   ```bash
   javac src/*.java -d out
   ```
4. Execute:

   ```bash
   java -cp out Main
   ```

---

## 📋 Funcionalidades

* **Criar nova conta**: registra conta com número gerado automaticamente.
* **Consultar conta**: exibe dados da conta e saldo atual.
* **Depositar**: permite adicionar valor ao saldo.
* **Sacar**: faz retirada, com validação de saldo.
* **Encerrar conta**: remove conta, se saldo é zero.
* **Validações robustas**: impede CPF, números ou valores inválidos.

---

## 📌 Aprendizados

* Estruturas de repetição (`while`, `for`).
* Condicionais (`if` / `else`).
* Tratamento de exceções (`try` / `catch`).
* Uso de classes e encapsulamento (POJOs).
* Entradas seguras pelo terminal com `Scanner`.
* Boas práticas no design de métodos e modularização do código.

---

## 🧪 Testes e melhorias futuras

* **Cobertura de testes** em JUnit para métodos da classe `Banco` e `Conta`.
* Interface gráfica (Swing/JavaFX).
* Adição de persistência em arquivos ou banco de dados.
* Operações bancárias avançadas (transferência, extrato).

---

## 📚 Referências

* Orientação do professor **Maicris Fernandes**.
* Apostilas e material didático da disciplina.
* Exemplos e padrões de mercado em Java.

---

## 📝 Autor

**Vitor N. Cordeiro** — estudante de Engenharia de Software.
Trabalho desenvolvido para a disciplina de Raciocínio Algorítmico (PFE).

---

## 📄 Licença

Este projeto é distribuído sob a [MIT License](LICENSE), garantindo liberdade de uso, modificação e distribuição.

```

---

### 🧩 Como usar este modelo

1. Crie um arquivo `README.md` na raiz do projeto.
2. Copie e cole o conteúdo acima.
3. Ajuste conforme necessário (nomes de classes, instruções de compilação, etc.).
4. Commit e push para atualizar o repositório.

Se quiser adicionar exemplos de execução, badges de estado (build, cobertura), integração contínua ou templates para issues/pull requests, posso te ajudar com isso também!
::contentReference[oaicite:0]{index=0}
```
