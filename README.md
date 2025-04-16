# ** Project - Data Generator **

Data Generator é uma aplicação simples e interativa desenvolvida em Python, que permite ao usuário gerar, visualizar e gerenciar dados fictícios de forma prática e rápida diretamente pelo terminal.

A proposta é simular um ambiente de geração de dados como nomes, e-mails, telefones, cidades e estados — tudo isso sendo salvo em um arquivo .txt de forma automatizada.

## 🎯 Funcionalidades

* 🆕 Geração de Dados Aleatórios: Cria nomes, e-mails, telefones e localizações fictícias com apenas um comando.
* 📂 Visualização de Dados: Permite visualizar todo o conteúdo salvo no arquivo de dados.
* 🧹 Limpeza de Arquivo: Remove todas as informações armazenadas no arquivo, deixando-o limpo.
* 🚪  Saída Segura: Finaliza o programa de forma elegante, preservando ou limpando os dados conforme a ação anterior.

## ⚙ Tecnologias Utilizadas

* 🐍 Python 3.12.10
* 📄 Armazenamento em arquivo .txt
* 💡 Uso de dicionários para simulação de banco de dados
* 💻 Execução 100% via terminal

## 📱 Interface

Menu de texto interativo com as seguintes opções:

### Menu Principal:

- (1) Ver Dados Gerados
- (2) Gerar Novos Dados
- (3) Esvaziar Arquivo
- (4) Sair do Programa

Cada opção é simples, direta e voltada para facilitar a experiência do usuário.

---

## 💡 Funcionalidades do Código

- **Uso de Dicionários:** Simula uma estrutura de banco de dados em memória.
- **Persistência em Arquivo:** Os dados são gravados e acessados por um arquivo .txt.
- **Execução no Terminal:** Toda a interface é feita via linha de comando, de forma simples e acessível.

## ▶ Como Executar o Projeto

### 📚 Requisitos

- Python 3 instalado na máquina
- Terminal ou prompt de comando configurado

### ♟ Passo a Passo

**Para utilizar o Data Generator no seu computador, siga os passos abaixo:**

```bash
# 1. Acesse o local onde você quer salvar o projeto
cd Desktop

# 2. Clone este repositório na sua máquina
git clone https://github.com/Dev-GAF/Data-Generator.git

# 3. Acesse a pasta do projeto
cd Data-Generator

# 4. Execute o programa
python app.py
```
💡 Importante:

- Se estiver usando o PowerShell no Windows, o comando python pode ser python3 em alguns casos.
- Se der erro de "python não é reconhecido", verifique se o Python está instalado e adicionado ao PATH.
- Certifique-se de estar dentro da pasta correta antes de rodar o python app.py.

### 📁 Estrutura do Projeto

```plaintext
Date-Generator/
├── app.py         // Arquivo principal que executa o programa
├── arquivo.py     // Responsável por salvar, mostrar e limpar os dados
├── interface.py   // Toda a parte que se usa o terminal (mais interativo para o usuário)
├── terminal.py    // Função para limpar o terminal
```

## 📋 License

### This project is licensed under the MIT License. See the LICENSE file for more details.
