
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

for i in range(1, numero):
    if numero  % i != 0:
        print(f"O número {numero} é  primo ")
    else:
        for i in range(1, numero):
            lista_divisiveis.append(i)
        print(f"Esse número não é primo, ele é divisivel por: {lista_divisiveis}")
        