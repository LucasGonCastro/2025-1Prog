#Dada uma plavra chave, o programa so deve parar de pedir quando o usuario o usuario digiar a palavra chave

Senha = "123mudar" 
entrada = "" 

while entrada != Senha:
    entrada = input(f"Digite uma palavra ('{Senha}'): ")
    if entrada != Senha:
        print("Você digitou incorretamente, tente novamente", entrada)

print("Você Digitou a Senha Corretamente")
