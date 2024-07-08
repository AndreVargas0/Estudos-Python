import os


while True: 
    os.system('cls') #limpar o terminal
    operacao = str(input("Qual operação você quer? Usar '+' para soma, '-' para subtração, '/' para divisão, '*' para multiplicação, deixe em branco para encerar a calculadora "))


    if operacao != "":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if  operacao == '+':
            print("Esse é o resultado da sua soma: ", num1 + num2)
        elif operacao == '-':
            print("Esse é o resultado da sua subtração: ", num1 - num2)
        elif operacao == '/':
            print("Esse é o resultado da sua divisão: ", num1 / num2)
        else:
            print("Esse é o resultado da sua multiplicação: ", num1 * num2)
    else:
        print("Calculadora finalizada")
        break

