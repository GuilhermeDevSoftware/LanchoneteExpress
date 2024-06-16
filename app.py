import os

restaurantes = [] #lista que recebe valores, seria o vetor em C

def cadastrar_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_restaurante) #esse é o comando que faz a lista receber o valor .append
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso\n')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def opcao_invalida():
    print('Opção inválida\n')
    input('Digite qualquer tecla para retornar ao menu: ')
    main()

def finalizar_app():
    os.system('cls')
    print('Finalizando o app\n')

def exibir_nome_programa():
    print("""
        
        
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        
        """)

def exibir_opcoes():
    print('1. Cadastrar restaurante: ')
    print('2. Listar: ')
    print('3. Ativar restaurante:')
    print('4. Sair: ')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))
        
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                print('Listar restaurantes')    
            case 3:
                print('Ativar restaurante') 
            case 4:
                finalizar_app()      
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()        
        

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
