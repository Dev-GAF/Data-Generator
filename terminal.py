from os import system, name

def limpar_terminal() -> None:
    """
    Limpa o terminal, utilizando o comando apropriado dependendo do sistema operacional.
    
    No Windows, o comando utilizado é 'cls', enquanto no Linux ou macOS, é 'clear'.
    
    return:
        None
    """
    
    sistema = name
    
    system('cls') if sistema=='nt' else system('clear')
    
    # if sistema == 'nt':
    #     system('cls')
    # else:
    #     system('clear')
