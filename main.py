from agenda import *
import time


def slowprint(texto, atraso=0.03):
    for c in texto:
        print(c, end='', flush=True)
        time.sleep(atraso)


slowprint('Olá usuário! Muito bem-vindo a sua agenda python, aqui vc poderá criar novos contatatos e manipulá-los.''\n''É importante saber que o cadastro é baseado no e-mail, portanto não é possível criar usuários que compartilham do mesmo e-mail ;)''\n')

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
        slowprint('\n''Uhuuu temos um novo contato''\n')
    elif resp == '2':
        lista_contatos()
        slowprint('\n''Aqui estão todos os contatos para você :)''\n')
    elif resp == '3':
        nome = input('Informe o nome dos contatos que você deseja procurar: ')
        busca_contato_nome(nome)
        slowprint('\n'f'Todos os contatos com o nome {nome} na sua mão :)''\n')
    elif resp == '4':
        email = input('Informe o Email do contato que você deseja procurar: ')
        busca_contato_email(email)
        slowprint('\n''Tá na mão!!! :)''\n')
    elif resp == '5':
        email = input('Informe o Email do contato que você deseja alterar: ')
        altera_contato(email)
        slowprint('\n''Nós da agenda python alteramos o contato para você :)''\n')
    elif resp == '6':
        email = input('Informe o Email do contato que você deseja excluir: ')
        exclui_contato(email)
        slowprint('\n'f'Uma pena dizer adeus aos contatos :(''\n')
    elif resp == '7':
        conf = input('Tem certeza que quer formatar sua agenda?''\n'
                     '1 - Sim''\n'
                     '2 - Não''\n')
        if conf == '1' or conf == 'Sim' or conf == 'sim':
            formatar_agenda()
            slowprint('\n''Adeus contatos ;(''\n')
        elif conf == '2' or conf == 'Nao' or conf == 'Não' or conf == 'nao' or conf == 'não':
            slowprint('\n''Operação cancelada com sucesso ;)''\n')
    elif resp == '8':
        carrega_contatos()
    elif resp == '9':
        break
    else:
        slowprint('Comando inválido :/''\n')

slowprint('Obrigado por utilizar a agenda python :)''\n')

input('Para sair da agenda aperte <Enter>')
