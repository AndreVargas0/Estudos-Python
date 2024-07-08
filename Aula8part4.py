#Crie um programa que liste 5 salas de cinema, e mostre o filme de cada uma das salas e suas classificações indicativas. O usuário deverá imformar sua idade e a sala 
#com o flime desejado. Caso o usuário não tenha a idade mínima, 
#o programa deverá informar que elenão tem idade para ver o filme, e deverá a lista de filmes para que o usuário escolha outro filme.
import os
import time 

print(36*"-", "CINEMA", 36*"-")

nome =input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
while True:
        os.system('cls') 
        print(30*"-", "FILMES DISPONIVEIS", 30*"-")
        print("Sala - 1: Deadpool e Wolverine. Classificação indicativa: 18")
        print("Sala - 2: Um lugar silencioso dia um. Classificação indicativa: 14")
        print("Sala - 3: Piratas do caribe a maldição do pérola negra . Classificação indicativa: 12")
        print("Sala - 4: Meu malvado favorito 4. Classificação indicativa: Livre")
        print("Sala - 5: Divertida mente 2. Classificação indicativa: Livre") 

        sala = int(input("Digite o número da sala do filme que você deseja assistir: "))
        os.system('cls') 
        if sala == 1 and idade >=18:
            break
        elif sala == 2 and idade >= 14:
            break
        elif sala == 3 and idade >= 12:
            break
        elif sala == 4 and idade >= 0:
            break
        elif sala == 5 and idade >= 0:
            break
        else:
            print("Você não tem idade para ver esse filme. Escolha outro filme!")
            time.sleep(3)
if sala == 1:
     filme = "Deadpool e Wolverine"
elif sala == 2:
     filme = "Um lugar silencioso dia um"
elif sala == 3:
     filme = "Piratas do caribe a maldição do pérola negra"
elif sala == 4:
     filme = "Meu malvado favorito 4"
else:
     filme = "Divertida mente 2"
    
cont = 0
while cont < 10:
    cont += 1
    if cont % 2 == 0:
        print("Imprimindo seu ingresso!")
        time.sleep(1)
    else:
        continue

os.system('cls') 
print(36*"-", "INGRESSO", 36*"-")
print(nome)
print(filme)
print("O assento é livre")
