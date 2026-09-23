#Faça um programa para ler um valor monetário (R$) de um produto e calcule um desconto de 10% se o valor do produto for inferior a R$ 5.000,00; o desconto a ser calculado, em caso contrário, deverá ser de 15%. Calcule, também, o valor final do produto e apresente os valores como mostrado na coluna 'Resultados'.

valor_produto = float(input(""))

valor_desconto = 0.0
if valor_produto < 5000.00:
    valor_desconto = valor_produto * 0.10
else:
    valor_desconto = valor_produto * 0.15

valor_produto_com_desconto = valor_produto - valor_desconto
valor_final = valor_produto - valor_desconto

print("Valor do Produto        = R$ {:.2f}".format(valor_produto))
print("Valor do Desconto ({:.0f}%) = R$ {:.2f}".format(valor_desconto / valor_produto * 100, valor_desconto))
print("Valor Final             = R$ {:.2f}".format(valor_final))
