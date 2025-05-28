base = int(input("Digite a Base = "))
potencia = int(input("Diga a Potencia = "))

resultado = 1
contador = 0

while contador < potencia:
    resultado *= base
    contador += 1

print(resultado)