#Entrada 2

valor_venda = float(input("Digite o Valor da Venda R$: "))
percentual = float(input("Informe a Comissão R%: "))

comissao = valor_venda * percentual / 100

print(f"O valor da comissão é R${comissao:.2f}")

#Nota 1 : Ler Nota de Aula 4,5
#Nota 2 : Valor Negativo
#Nota 3 : Teste com Comissoes Positivas
#Nota 4 : Tratamento de Erro
