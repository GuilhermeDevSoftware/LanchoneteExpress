import os

restaurantes = [ #Isso é um dicionário dentro de uma lista
        {'nome':'Bonjour', 'categoria':'Pizzaria', 'ativo':False},
        {'nome':'Casa da Carne', 'categoria':'Churrascaria', 'ativo':True},
        {'nome':'Café Arte', 'categoria':'Cafeteria', 'ativo':False}
] 

def exibir_nome_programa():
    '''Essa função é responsavel para mostrar o nome do programa'''
    print("""
        
        
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        
        """)

def voltar_menu():
    ''' Essa função é responsavel para voltar ao menu do programa
        Input: Tecla para voltar ao menu
    '''

    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def exibir_subtitulo(texto):
    '''Essa função é responsavel para mostrar o subtitulo do programa'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)

def cadastrar_restaurante():
    ''' Essa função é responsavel para cadastrar um restaurante por vez

        Inputs:
        Nome do restaurante
        Categoria

        Output:
        Adiciona um novo restaurante a lista
    '''
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False} #dicionario
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso\n')
    voltar_menu()

def listar_restaurante():
    ''' Essa função é responsavel para listar os restaurantes cadastrados'''
    exibir_subtitulo('Listando restaurantes: \n')
        #variavel declarada no laço
    print(f'{" Nome do Restaurante".ljust(20)}  | {"Categoria".ljust(20)} | Status')  
    for restaurante in restaurantes: #lista
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado' #ternario
        print(f'-{nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo_restaurante}')   
    voltar_menu()               # .ljust da um espaçamento para o lado

def alternar_estado():
    ''' Essa função é respnsavel para mudar o status de ATIVO ou INATIVO do restaurante

        Input:
        Nome do restaurante
    '''
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O {nome_restaurante} foi desativado'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')        
    voltar_menu()

def opcao_invalida():
    '''Essa função é responsavel para invalidar uma ação'''
    print('Opção inválida\n')
    voltar_menu()

def exibir_opcoes():
    '''Essa função é responsavel para exibir as opções do app'''
    print('1. Cadastrar restaurante: ')
    print('2. Listar: ')
    print('3. Ativar/Desativar restaurante:')
    print('4. Sair: ')

def escolher_opcao():
    '''Essa função é responsavel para escolher a ação desejada'''
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))
        
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurante()    
            case 3:
                alternar_estado()
                voltar_menu()
            case 4:
                finalizar_app()      
            case _:
                opcao_invalida()
    except ValueError:
        opcao_invalida()        

def finalizar_app():
    '''Essa função finaliza o app'''
    exibir_subtitulo('Finalizando o app\n')        

def main():
    '''Função principal do programa'''
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
