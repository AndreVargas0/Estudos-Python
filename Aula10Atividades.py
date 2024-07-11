
''' desafio 1
contagem = 0
soma = 0

for i in range(1,100):
    if i % 2 != 0:
        contagem += 1
        soma = i + soma
print(f"A soma dos números impares foi: {soma}")
print(f"Foram encontrados {contagem} ")
'''


''' desafio 2
    import os
import time 

print(30*"-","LISTA DE TAREFAS",30*"-")
tarefas = []
while True:
    nova_tarefa = str(input("Digite a tarefa que deseja adicionar: Deixe em branco para finalizar e mostrar sua lista. "))
    if nova_tarefa != "":
        tarefas.append(nova_tarefa)
        os.system("cls")
    else:
        break

os.system("cls")

print("Essas são as suas tarefas: ")
for i in tarefas:
    print(i)
'''


numero = int(input("Digite o numero que você deseja saber se é primo: "))


lista_divisiveis = []
primo =True
cont = 0

for i in range(2,numero):
    if (numero % i == 0):
        cont +=1
        lista_divisiveis.append(i)
        
        primo = False
if primo == True:
    print("Esse número é primo")
else:
    print(f"Esse número não é primo, ele é divisivel por {cont} números e eles são: {lista_divisiveis}") 