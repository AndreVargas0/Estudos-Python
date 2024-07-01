''' print("Hello world!") '''

#comentario de linha
'''
comentario de bloco
'''

'''
nome = "André"
print("Esse é o meu nome:", nome)
peso = 80.5
altura = 1.78
instrutor = True
print(peso, type (peso))
print(altura, type(altura))
print (instrutor, type(instrutor))

'''
valor = 15
print(valor, type(valor))
valor = str(valor)
print(valor, type(valor))

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
ano =int(input("Digite o ano em que você está: "))
if ano>2023:
    print(f"Ola, meu nome é: {nome} e tenho {idade} anos de idade e posso fumar maconha")
else:
    print("Ola, meu nome é: "+ nome + " e tenho " + str(idade) + " anos de idade e não posso fumar maconha")