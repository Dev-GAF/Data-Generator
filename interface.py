from time import sleep
from typing import Union

# Função para formatar e exibir as opções de menu
def formatar_menus(lista_num_opcoes) -> None:
    """
    Exibe as opções de menu de forma numerada no terminal.
    
    Params:
    lista_num_opcoes (list): Lista de opções a serem exibidas no menu.
    
    return:
    None
    """
    for valor, campo in enumerate(lista_num_opcoes):
        print(f"[{valor+1}] - {campo}")

# Função que cria uma lista de números de 1 até o número recebido
def transformar_em_lista(qtd) -> list:
    """
    Retorna uma lista com números de 1 até 'qtd'.
    
    Params:
    qtd (int): O número até o qual a lista será gerada.
    
    return:
    list: Lista com números de 1 até 'qtd'.
    """
    lista = []
    for valor in range(1, qtd+1):
        lista.append(valor)
    return lista

# Função para criar uma linha de separação
def linha(tam=40) -> str:
    """
    Retorna uma linha de caracteres "=" com o tamanho especificado (padrão 40).
    
    Params:
    tam (int): O tamanho da linha de separação (padrão é 40).
    
    return:
    str: A linha de separação formada por caracteres "=".
    """
    return "="*tam

# Função que alinha um título no centro, com base no tamanho da linha
def alinhar_titulo(titulo) -> str:
    """
    Alinha o título no centro da linha de separação.
    
    Params:
    titulo (str): O título que será centralizado.
    
    return:
    tuple: A linha de separação e o título centralizado.
    """
    lin = linha()
    largura_titulo = len(titulo)
    largura_linha = len(lin)
    espacos = (largura_linha - largura_titulo) // 2
    novo_titulo = ' '*espacos + titulo + ' '*espacos
    return "=" * largura_linha, novo_titulo

# Função para exibir o título com linha superior e inferior
def inserir_linha_e_titulo(titulo="Qualquer coisa") -> None:
    """
    Exibe o título com linhas de separação antes e depois.
    
    Params:
    titulo (str): O título a ser exibido (padrão é "Qualquer coisa").
    
    return:
    None
    """
    lin, texto = alinhar_titulo(titulo)
    print(lin)
    print(texto)
    print(lin)

# Função que exibe o cabeçalho do programa (menu principal)
def cabecalho(titulo="MENU PRINCIPAL") -> None:
    """
    Exibe o cabeçalho com o título fornecido.
    
    Params:
    titulo (str): O título do cabeçalho (padrão é "MENU PRINCIPAL").
    
    return:
    None
    """
    inserir_linha_e_titulo(titulo)

# Função para exibir as opções do menu
def opcoes_menu() -> list:
    """
    Exibe as opções de menu e retorna a opção selecionada pelo usuário.
    
    return:
    list: A opção escolhida pelo usuário.
    """
    campos = ['Ver Dados Gerados', 'Gerar Novos Dados', 'Esvaziar Arquivo', 'Sair do Programa']
    formatar_menus(campos)
    lin = linha()
    print(lin)
    tam_campos = len(campos)
    lista_num_opcoes = transformar_em_lista(tam_campos)
    msg_opcao = 'Sua opcao: '
    return verifica_opcao(lista_num_opcoes, msg_opcao, False)

# Função para verificar se a opção inserida pelo usuário é válida
def verifica_opcao(lista_num_opcoes, texto, mult_opcoes=False) -> list:
    """
    Verifica se a opção inserida pelo usuário é válida.
    Permite selecionar múltiplas opções caso 'mult_opcoes' seja True.
    
    Params:
    lista_num_opcoes (list): Lista com as opções válidas.
    texto (str): Mensagem exibida ao solicitar a opção.
    mult_opcoes (bool): Define se o usuário pode escolher múltiplas opções (padrão é False).
    
    return:
    list: Lista com as opções válidas selecionadas pelo usuário.
    """
    while True:
        opcoes = capturar_entrada(texto, str)
        lista_opcoes_verificadas = []
        if mult_opcoes:
            lista_opcoes = opcoes.split(",")
            for opcao in lista_opcoes:
                opcao = opcao.strip()
                if opcao.isdigit() and int(opcao) in lista_num_opcoes:
                    lista_opcoes_verificadas.append(int(opcao))
                else:
                    print(f"\nErro! Digite apenas números naturais e dentro das opções.")
                    print(f"Em caso de mais de uma opção, digite assim: 1, 2..., 5\n")
                    break
            if len(lista_opcoes_verificadas)==len(lista_opcoes):
                return lista_opcoes_verificadas
        else:
            if opcoes.isdigit() and int(opcoes) in lista_num_opcoes:
                return [int(opcoes)]
            raise ValueError(f"Digite uma das opções oferecidas.")  

# Função para capturar a entrada do usuário
def capturar_entrada(msg_opcao, tipo=int) -> Union[int, str]:
    """
    Captura a entrada do usuário com base no tipo esperado (int ou str).
    
    Params:
    msg_opcao (str): Mensagem exibida para solicitar a entrada.
    tipo (type): Tipo de dado esperado (int ou str).
    
    return:
    Union[int, str]: A entrada do usuário convertida para o tipo esperado.
    """
    if tipo not in [int, str]:
        print(f"Erro! Tipo esperado inválido. \nPossível erro localizado em: \"verifica_opcao()\"")
        exit(0)
    
    while True:
        opcao = input(msg_opcao).strip()
        
        if tipo == int:
            if opcao.isdigit():
                return int(opcao)
            raise ValueError(f"Erro! Digite apenas um número natural.")
        elif tipo == str:
            if opcao:
                return opcao
            raise ValueError(f"Erro! Digite um valor válido.")
        
# Função para exibir os dados gerados, se houver
def dados_gerados(titulo="DADOS GERADOS") -> None:
    """
    Exibe os dados que foram gerados ou uma mensagem caso não haja dados.
    
    Params:
    titulo (str): O título a ser exibido (padrão é "DADOS GERADOS").
    
    return:
    None
    """
    from arquivo import mostrar_dados
    inserir_linha_e_titulo(titulo)
    
    if not mostrar_dados():
        print("Nenhum Dado Existente.")
    
    lin = linha()
    print(lin)
    print("Pressione Enter para continuar...")
    input()

# Função para gerar novos dados de acordo com a escolha do usuário
def gerar_dados(titulo="GERAMENTO DE DADOS") -> list:
    """
    Exibe as opções para gerar novos dados (nome, e-mail, telefone, cidade, estado).
    Retorna os dados gerados.
    
    Params:
    titulo (str): O título a ser exibido (padrão é "GERAMENTO DE DADOS").
    
    return:
    list: Lista de dados gerados conforme a escolha do usuário.
    """
    campos = ['Nome', 'E-mail', 'Telefone', 'Cidade', 'Estado']
    inserir_linha_e_titulo(titulo)
    
    print("Escolha uma ou mais opções abaixo:")
    formatar_menus(campos)
    lin = linha()
    print(lin)
    tam_campos = len(campos)
    lista_num_opcoes = transformar_em_lista(tam_campos)
    msg_opcao = 'Opção(ões) de Cadastro: '

    opcoes_verificadas = verifica_opcao(lista_num_opcoes, msg_opcao, True)

    dado_gerado = []
    for valor in opcoes_verificadas:
        dado = sortear_dados(valor)
        dado_gerado.append(dado)
    
    return dado_gerado

# Função que sorteia dados de acordo com a opção escolhida
def sortear_dados(opcao) -> str:
    """
    Sorteia e retorna um dado com base na opção escolhida.
    
    Params:
    opcao (int): O número da opção escolhida.
    
    return:
    str: O dado sorteado.
    """
    from random import choice
    dados = {
        1: ['André', 'Roberto', 'Carlos', 'Fernanda', 'Marcos'],
        2: ['andre.58@outlook.com', 'roberto.24@gmail.com', 'carlos.15@yahoo.com', 'fernanda.38@hotmail.com', 'marcos.72@gmail.com'],
        3: ['(51) 9934-5678', '(21) 9987-6543', '(11) 9876-5432', '(31) 9998-1234', '(41) 9887-2345'],
        4: ['São Paulo', 'Belo Horizonte', 'Porto Alegre', 'Curitiba', 'Salvador'],
        5: ['SP', 'MG', 'RS', 'PR', 'BA']
    }
    
    if 1 <= opcao <= 5:
        return choice(dados[opcao])

# Função para esvaziar o arquivo de dados
def esvaziar_arquivo(titulo="Esvaziando arquivo...") -> None:
    """
    Esvazia o arquivo de dados e exibe uma mensagem de sucesso.
    
    Params:
    titulo (str): O título a ser exibido (padrão é "Esvaziando arquivo...").
    
    return:
    None
    """
    inserir_linha_e_titulo(titulo)
    sleep(1)
    print("Arquivo Esvaziado com Sucesso!")
    sleep(1.5)

# Função para encerrar o programa
def encerrar_programa(titulo="PROGRAMA ENCERRADO") -> None:
    """
    Exibe uma mensagem de encerramento e limpa o terminal.
    
    Params:
    titulo (str): O título a ser exibido (padrão é "PROGRAMA ENCERRADO").
    
    return:
    None
    """
    from terminal import limpar_terminal
    print("Encerrando...")
    sleep(0.5)
    limpar_terminal() 
    inserir_linha_e_titulo(titulo)
