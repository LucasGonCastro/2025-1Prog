
import sys

Distancia = int(input("Insira a Distancia Percorrida em KM: "))
if Distancia <=0:
    sys.exit('Informe a Distancia Positiva')

Velocidade = int(input("Insira a Velocidade em KM/H: "))
if Velocidade <=0:
    sys.exit("Informe a Velocidade De Forma Positiva")
    
Acelera = int(input("Insira a aceleração em M/S ^2: "))
if Acelera <=0:
    sys.exit("informe a Aceleração Positiva")

Distancia *=1000
Velocidade /=3.6

Delta = Velocidade**2 -4*Acelera*Distancia
if Delta<0:
    sys.exit("Não é possivel calcular o tempo")

T = (-Velocidade+Delta**0.5)/(2*Acelera)
hora = T//3600
T= T%3600
Minuto = T//60
Segundo = T%60
Print(f"Tempo ={hora}={Minuto}={Segundo}")