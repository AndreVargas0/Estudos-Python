import os
import time 

print(36*"-", "CINEMA", 36*"-")

nome =input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
while True:
        os.system('cls') 
        print(30*"-", "FILMES DISPONIVEIS", 30*"-")
        print("Sala - 1: Deadpool e Wolverine. ", 31 * "_"," Classificação indicativa: 18")
        print("Sala - 2: Um lugar silencioso dia um.", 26 * "_"," Classificação indicativa: 14") 
        print("Sala - 3: Piratas do caribe a maldição do pérola negra.", 8 * "_"," Classificação indicativa: 12")
        print("Sala - 4: Meu malvado favorito 4.", 30 * "_"," Classificação indicativa: Livre")
        print("Sala - 5: Divertida mente 2.", 35 * "_"," Classificação indicativa: Livre") 

        sala = int(input("Digite o número da sala do filme que você deseja assistir: "))
        os.system('cls') 
        if sala == 1 and idade >=18:
            filme = "Deadpool e Wolverine"
            break
        elif sala == 2 and idade >= 14:
            filme = "Um lugar silencioso dia um"
            break
        elif sala == 3 and idade >= 12:
            filme = "Piratas do caribe a maldição do pérola negra"
            break
        elif sala == 4 and idade >= 0:
            filme = "Meu malvado favorito 4"
            break
        elif sala == 5 and idade >= 0:
            filme = "Divertida mente 2"
            break
        else:
            print("Você não tem idade para ver esse filme. Escolha outro filme!")
            time.sleep(3)
 
cont = 0
while cont < 5:
    cont += 1
    print("Imprimindo seu ingresso!")
    time.sleep(1)
    continue

os.system('cls') 
print(36*"-", "INGRESSO", 36*"-") 
print(nome)
print(filme)
print("O assento é livre")
print(82*"-")
