import random

lista = [random.randint(1, 100) for _ in range(5)]

def main():
    def adicionar_numero(lista):
        y = input("digite um numero: ")
        lista.append(n)
        print(f"numero {y} foi adicionado a lista.")

    def remover_numero(lista):
        try:
            x = input("digite um numero: ")
            lista.remove(lista)
            print(f"numero {x} removido da lista.")
        except ValueError:
            print(f"erro: O numero {lista} nao esta na lista.")

    def exibir_lista():
        print(f"numeros da lista: {lista}")

    def somalista():
        soma = sum (lista) 
        print(f"soma da lista: {soma}")

    def medialista():
        media = soma / len(lista)
        print(f"media da lista: {media}")

    while True:
        print("escolha uma opção:")
        print("1- adicionar um numero a lista")
        print("2- remover um numero da lista")
        print("3- exibir a lista atual")
        print("4- calcular a soma dos numeros da lista")
        print("5- calcular a media dos numeros da lista")
        print("6- encerrar")

        operacao = input("digite a opçao desejada: ")

        if operacao == '1':
            adicionar_numero(lista)
        elif operacao == "2":
            remover_numero(lista)