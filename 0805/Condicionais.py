#Programa Calculo de Media de Diiciplina
#As Notas Devem Ser Intenrias E Entre 0 a 1000(Inclusive).

#Caso a Média seja igual ou superior a 60 o aluno estará aprovado;Caso o Média seja igual ou superior a 20 o aluno estará em Prova Final e os demais casos o aluno estará Reprovado

import sys

etapa1 = int(input("Insira a Nota da Etapa1: "))   
if etapa1 < 0 or etapa1 > 100:
     sys.exit("ERRO: NOTA ETAPA 1 INVALIDA")

etapa2 = int(input("informe a Nota da Etapa 2: "))
if etapa2 < 0 or etapa2 > 100:
     sys.exit("ERRO NOTA ETAPA 2 INVALIDA ")

media = round ( (etapa1 * 2 + etapa2 * 3) / 5 )
print(f"Media Do Aluno:{media}")

if media >= 60:
    print("Aluno Aprovado")
elif media >=20:
    print("Prova Final")
else:
    print("Reprovado")