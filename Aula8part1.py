import os
import time

cont = int(input("Digite um núero inteiro: "))

while cont >= 0:
    os.system('cls') #limpar o terminal
    print(f"Contagem refressiva: {cont} ...")
    time.sleep(1) #atrassa o proximo comando
    cont -= 1
os.system('cls')
print('BOOOOOOOOOOOOOOOOMMMMMMM!!!!!!')