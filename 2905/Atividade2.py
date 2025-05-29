from logging import exception
from multiprocessing.sharedctypes import Value
import sys
try:
    intValor = int(input("Digite o Valor: "))
except ValueError:
    sys.exit("Erro de Valor")
except exception as e:
    sys.exit("Erro Inesperado: {e} ")
else:
    if intValor < 0:
        print("Não Existe Fatorial")
    else:
        if:
            intValor <2:
                print(f"{intValor}"=1")
                
