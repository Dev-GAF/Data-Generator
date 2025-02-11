from interface import *
from arquivo import *

from terminal import limpar_terminal

if __name__ == "__main__":
    
    acabou=False
    while not acabou:
        try:
            limpar_terminal()
            
            cabecalho()
            
            opcao = opcoes_menu()
            
            for valor in opcao:
                if valor == 1:
                    # Limpa o terminal e exibe os dados gerados
                    limpar_terminal()
                    
                    dados_gerados()
                    
                elif valor == 2:
                    # Limpa o terminal e gera novos dados
                    limpar_terminal()
                    
                    dado_gerado = gerar_dados()
                    
                    salvando_dados(dado_gerado)
                    
                elif valor == 3:
                    # Limpa o terminal e esvazia o arquivo
                    limpar_terminal()
                    limpar_dados()
                    
                    esvaziar_arquivo()
                    
                else: # Validado para ser 4
                    encerrar_programa()
                    acabou=True
                    
        except ValueError as erro:
            print(f"Erro: {erro}")
            print(f"\nPressione Enter para tentar novamente...")
            input()
    



