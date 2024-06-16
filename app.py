import os

restaurantes = [ #Isso é um dicionário dentro de uma lista
        {'nome':'Bonjour', 'categoria':'Pizzaria', 'ativo':False},
        {'nome':'Casa da Carne', 'categoria':'Churrascaria', 'ativo':True},
        {'nome':'Café Arte', 'categoria':'Cafeteria', 'ativo':False}
] 

def exibir_nome_programa():
    print("""
        
        
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        
        """)

def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False} #dicionario
    restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso\n')
    voltar_menu()

def listar_restaurante():
    exibir_subtitulo('Listando restaurantes: \n')
        #variavel declarada no laço
    for restaurante in restaurantes: #lista
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = restaurante['ativo']
        print(f'-{nome_restaurante} | {categoria_restaurante} | {ativo_restaurante}')   
    voltar_menu()

def alternar_estado():
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
    print('Opção inválida\n')
    voltar_menu()

def exibir_opcoes():
    print('1. Cadastrar restaurante: ')
    print('2. Listar: ')
    print('3. Ativar/Desativar restaurante:')
    print('4. Sair: ')

def escolher_opcao():
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
    exibir_subtitulo('Finalizando o app\n')        

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
