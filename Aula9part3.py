import random
import os

numero_secreto = random.randint(1,20)

tentaiva = 0
max_tentativa = 5
acertou = False

print("Bem-vindo ao GAME Python Adivinha!!!!!")
print(f"Você tem {max_tentativa} tentatativas para adivinhar o número secreto entre 1 e 20")


while tentaiva < max_tentativa:
    palpite = int(input(f"Digite o número da sua {tentaiva + 1}°: "))
    tentaiva =  tentaiva + 1
    if palpite == numero_secreto:
        acertou = True
        break
    elif palpite < numero_secreto:
        print("O número é maior")
    else:
        print("O número é menor")

os.system('cls') 


if acertou == True:
    print("Você acertou!!!!😊")
else:
    print(f"Você errou!!!!😢, o número era {numero_secreto}")