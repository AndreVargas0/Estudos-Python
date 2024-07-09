import random
import os

cont = 1

lista_sorteados =[]
lista_nome = []

while True:
    nome = input(f"Digite o {cont}º nome que será sortidado:  Deixe em branco para finalizar a adição de nomes ")
    cont = cont + 1
    if nome != "":
        lista_nome.append(nome)
    else:
        break

while True: 
    if lista_nome:
        os.system('cls')
        escolhido = random.choice(lista_nome)
        lista_sorteados.append(escolhido)
        print(f"O sorteado é {escolhido}")

        opcao = input("Deseja sortear outro nome (s/n)").lower
        os.system('cls')

        if opcao!= "s" :
            break
    else:
     print("Não existe nomes para serem sorteados")

print("Programa finalizado")
print(f"Lista dos nomes{lista_nome}")
print(f"Lista dos nomes{lista_sorteados}")
