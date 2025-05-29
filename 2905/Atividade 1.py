from logging import exception
import sys

try:
    intValor= int(input("Digite o Numero: "))
except ValueError:
    sys.exit("Digite um valor valido")
except exception as e:
    sys.exit(f"Erro Inesperado {e}")
else:
    intCntDiv = 1
    intDivisior = 2
    while intDivisior <=intValor:
        if intValor % intDivisior == 0:
            intCntDiv += 1
        if intCntDiv >2: break
        intDivisior += 1
        if intCntDiv ==2:
            print("Primo")
        else:
            print("Não Primo")

