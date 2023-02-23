from prettytable import PrettyTable
import requests
import json

from banco_dados import salva_contato, busca_contatos, busca_por_nome, busca_por_email, deleta_contato, limpa_agenda
from contato import Contato


contatos = []


def novo_contato():
    nome = input("Digite um nome para o contato: ")
    email = input("Digite um email para o contato: ")
    telefone = input("Digite um telefone para o contato (xx xxxxx-xxxx): ")

    contato = busca_contato_email(email)

    if contato:
        print(f"O email {email} já esta cadastrado")
        return

    salva_contato(Contato(nome, email, telefone))

    lista_contatos()


def lista_contatos():
    table = PrettyTable(["Nome", "Email", "Telefone"])

    for contato in busca_contatos():
        table.add_row([contato.nome, contato.email, contato.telefone])
    print(table)


def busca_contato_nome(nome):
    table = PrettyTable(["Nome", "Email", "Telefone"])

    for contato in busca_por_nome(nome):
        table.add_row([contato.nome, contato.email, contato.telefone])

    print(table)


def busca_contato_email(email):
    resultado = busca_por_email(email)

    if not resultado:
        return

    return resultado


def altera_contato(email):
    contato = busca_contato_email(email)

    if not contato:
        print(f"Não existe o contato com o email: {email}")
        return

    nome = input("Digite um nome para o contato: ")
    telefone = input("Digite um telefone para o contato (xx xxxxx-xxxx): ")

    contato.nome = nome
    contato.telefone = telefone

    lista_contatos()


def exclui_contato(email):

    contato = busca_contato_email(email)

    if not contato:
        print(f"Não existe um contato com o email: {email}")
        return

    deleta_contato(email)

    lista_contatos()


def formatar_agenda():
    limpa_agenda()
    lista_contatos()
    pass


def carrega_contatos():
    response = requests.get("https://randomuser.me/api")

    resultado = response.json()

    contato = Contato(nome="{}{}".format(
        resultado['results'][0]['name']['first'],
        resultado['results'][0]['name']['last']),
        email=resultado['results'][0]['email'],
        telefone=resultado['results'][0]['phone'])

    salva_contato(contato)

    lista_contatos()
