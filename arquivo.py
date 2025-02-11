# Função para salvar dados em um arquivo
def salvando_dados(dados) -> None:
    """
    Salva os dados recebidos no arquivo 'arquivo.txt'. 
    Os dados são adicionados ao final do arquivo, um por linha.
    
    Params:
    dados (list): Lista contendo os dados a serem salvos no arquivo.
    
    return:
    None
    
    except:
    IOError: Se ocorrer algum erro ao tentar abrir ou escrever no arquivo.
    """
    from time import sleep

    try:
        manipulador = open('arquivo.txt', 'a', encoding='utf-8')
        
        print("Gerando dados...")
        sleep(1.5)
        
        for dado in dados:
            manipulador.write(f"{dado}\n")
        
        print(f"\nDados Gerados com Sucesso!")
        sleep(1.5)
    
    except IOError:
        print("Não foi possível abrir o arquivo")
    else:
        manipulador.close()

# Função para mostrar os dados salvos no arquivo
def mostrar_dados() -> bool:
    """
    Exibe os dados armazenados no arquivo 'arquivo.txt'. 
    Retorna False se o arquivo estiver vazio, True caso contrário.
    
    return:
    bool: True se o arquivo contém dados, False caso contrário.
    """
    with open('arquivo.txt', 'r', encoding='utf-8') as arq:
        linhas = arq.readlines()
        
        if not linhas:
            return False
        
        for linha in linhas:
            print(linha, end='')
    
    return True

# Função para limpar todos os dados do arquivo
def limpar_dados() -> None:
    """
    Limpa o conteúdo do arquivo 'arquivo.txt', deixando-o vazio.
    
    return:
    None
    """
    with open('arquivo.txt', 'w', encoding='utf-8') as arq:
        
        pass
