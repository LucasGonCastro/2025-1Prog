'''
   Fazer um programa que:
   
      1) Solicite ao usuário um valor inteiro N positivo (valor máximo para N -> 100);

      2) Gere uma lista com N valores inteiros aleatórios entre -100 e +100;
   
      3) A partir da lista gerada, gere uma segunda uma lista apenas com os 
         números pares da lista;
'''
import sys, random

try:
    intN = int(input('Informe o valor de N: '))
except ValueError:
    sys.exit('/nERRO: Informe um valor inteiro válido...')
except Exception as e:
    sys.exit(f'ERRO:{e}')
else:
    numeros = list(range(-100, 101))
    lista = random.sample(numeros , intN)
    print(f'lista:{lista}')