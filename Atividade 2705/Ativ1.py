#Programa para executar um produto de números inteiros positivos utilizando apenas o operador soma (X)
x = int(input("Digite o Primeiro Numero"))
y = int(input("Digite o Segundo Numero"))
produto = x * y 
soma = 0

while soma < produto:
    soma += y
    print(f"{x}+{y}")
print(soma)