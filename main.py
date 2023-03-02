from agenda import *

print('Olá usuário! Muito bem-vindo a sua agenda python, aqui vc poderá criar novos contatatos e manipulá-los, é importante saber que o cadastro é baseado no e-mail, portanto não é possível criar usuários que compartilham do mesmo e-mail ;)')

resp = ''

while resp != '9':
    resp = input('O que gostaria de fazer na sua agenda?''\n'
                 '1 - Criar novo contato''\n'
                 '2 - Mostrar seus contatos''\n'
                 '3 - Buscar contatos por um nome''\n'
                 '4 - Buscar contato por Email''\n'
                 '5 - Alterar contato''\n'
                 '6 - Excluir contato''\n'
                 '7 - Formatar agenda''\n'
                 '8 - Criar contato aleatório''\n'
                 '9 - Sair''\n')
    if resp == '1':
        novo_contato()
    elif resp == '2':
        lista_contatos()
    elif resp == '3':
        nome = input('Informe o nome do contato que você deseja procurar: ')
        busca_contato_nome(nome)
    elif resp == '4':
        email = input('Informe o Email do contato que você deseja procurar: ')
        busca_contato_email(email)
    elif resp == '5':
        email = input('Informe o Email do contato que você deseja alterar: ')
        altera_contato(email)
    elif resp == '6':
        email = input('Informe o Email do contato que você deseja excluir: ')
        exclui_contato(email)
    elif resp == '7':
        conf = input('Tem certeza que quer formatar sua agenda?''\n'
                     '1 - Sim''\n'
                     '2 - Não''\n')
        if conf == '1' or conf == 'Sim' or conf == 'sim':
            formatar_agenda()
        elif conf == '2' or conf == 'Nao' or conf == 'Não' or conf == 'nao' or conf == 'não':
            print('Operação cancelada')
    elif resp == '8':
        carrega_contatos()
    elif resp == '9':
        break
    else:
        print('Comando inválido :/')

print('Obrigado por utilizar a agenda python :)')

input('Para sai da agenda aperte <Enter>')
