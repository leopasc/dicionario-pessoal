import os

dados = []


# Opção Inválida
def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

# Voltar ao menu
def voltar_ao_menu_principal():
    input('\nDigite ENTER para voltar ao menu principal')
    main()

# Nome do programa
def nome_do_programa():
    print("""
██████╗░██╗░█████╗░██╗░█████╗░███╗░░██╗░█████╗░██████╗░██╗░█████╗░
██╔══██╗██║██╔══██╗██║██╔══██╗████╗░██║██╔══██╗██╔══██╗██║██╔══██╗
██║░░██║██║██║░░╚═╝██║██║░░██║██╔██╗██║███████║██████╔╝██║██║░░██║
██║░░██║██║██║░░██╗██║██║░░██║██║╚████║██╔══██║██╔══██╗██║██║░░██║
██████╔╝██║╚█████╔╝██║╚█████╔╝██║░╚███║██║░░██║██║░░██║██║╚█████╔╝
╚═════╝░╚═╝░╚════╝░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░╚════╝░

██████╗░███████╗░██████╗░██████╗░█████╗░░█████╗░██╗░░░░░
██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██║░░░░░
██████╔╝█████╗░░╚█████╗░╚█████╗░██║░░██║███████║██║░░░░░
██╔═══╝░██╔══╝░░░╚═══██╗░╚═══██╗██║░░██║██╔══██║██║░░░░░
██║░░░░░███████╗██████╔╝██████╔╝╚█████╔╝██║░░██║███████╗
╚═╝░░░░░╚══════╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝""")

def frases_iniciais():
    print('Escolha a opção que deseja\n')
    print('1 - Nome')
    print('2 - Idade')
    print('3 - Nascimento')
    print('4 - Cidade')
    print('5 - País')
    print('6 - Mãe')
    print('7 - Pai')
    print('8 - Gatos')
    print('9 - Geral')


def main():
    os.system('cls')
    nome_do_programa()
    frases_iniciais()
    escolher_opcao()

    
def escolher_opcao():
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            print('\n Leonardo')
            voltar_ao_menu_principal()
        elif opcao_escolhida == 2: 
            print('\n18 Anos')
            voltar_ao_menu_principal()
        elif opcao_escolhida == 3: 
            print('\n24/02/2006')
            voltar_ao_menu_principal()
        elif opcao_escolhida == 4: 
            print('\nBarueri')
            voltar_ao_menu_principal()
        elif opcao_escolhida == 5: 
            print('\nBrasil')
            voltar_ao_menu_principal()
        elif opcao_escolhida == 6: 
            print('Josimara')
            voltar_ao_menu_principal()
        elif opcao_escolhida == 7: 
            print('Roberto')
            voltar_ao_menu_principal()
        elif opcao_escolhida == 8: 
            print('Suzy, Nick e Scrappy')
            voltar_ao_menu_principal()
        elif opcao_escolhida == 9: 
            print("""
Leonardo tem 18 Anos e nasceu em 24/02/2006.
Mora na cidade de Barueri, SP - Brasil. 
Seus pais se chamam Josimara e Roberto. 
Ele possuí 3 gatos, chamados: Suzy, Nick e Scrappy!""")
            voltar_ao_menu_principal()
        else: 
            opcao_invalida()
    except:
        opcao_invalida()

if __name__ == '__main__':
    main()
