#Entrada 2

valor_venda = float(input("Digite o Valor da Venda R$"))
percentual = float(input("Informe a Comissão R%"))

comissao = valor_venda * percentual / 100

print(f"O valor da comissão é R${comissao:.2f}")