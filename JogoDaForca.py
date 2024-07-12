import random
import os
import time

palavras = ["input", "python", "openai", "programação", "tecnologia", "desenvolvedor","garoto de programa", "algoritimo","software", "computador", "programas"]

palavras_secreta = random.choice(palavras)

lista_corretas=[]
lista_erradas=[]
tentativas=6

x = len(palavras_secreta)

while True:

    palavra_escondida = ""
    for letra in palavras_secreta:
        if letra in lista_corretas:
            palavra_escondida += letra
        else: 
            palavra_escondida += '_'

    print("Palavra: ", palavra_escondida)
    print("Letras erradas: ",lista_erradas)
    print("Tentativas restantes: ",tentativas)

    if palavra_escondida == palavras_secreta:
        os.system("cls")
        print("Parabéns você conseguiu!!!!!")
        break
    elif tentativas ==0:
        print("Você perdeu😢")
        print("A palavra era: ",palavras_secreta)
        break

    letra_usuario = input("Digite uma letra: ").lower()

    if letra_usuario in palavras_secreta:
        print("Letra correta!")
        lista_corretas.append(letra_usuario)
        time.sleep(2)
        os.system("cls")
    else:
        print("Letra errada!")
        lista_erradas.append(letra_usuario)
        tentativas -= 1
        time.sleep(2)
        os.system("cls")

