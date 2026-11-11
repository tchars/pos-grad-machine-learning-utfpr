# Faça um programa para ler um valor monetário (R$) de um produto e calcule um desconto fixo de 10%. Calcule também o valor final do produto. Apresente os valores como apresentado na coluna “Resultados”.

valor_produto = float(input(""))
desconto = valor_produto * 0.10
valor_final = valor_produto - desconto

print("Valor do Produto  = R$ {:.2f}".format(valor_produto))
print("Valor do Desconto = R$ {:.2f}".format(desconto))
print("Valor Final       = R$ {:.2f}".format(valor_final))
