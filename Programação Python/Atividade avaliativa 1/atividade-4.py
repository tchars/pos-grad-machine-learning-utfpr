# Faça um programa para ler um número inteiro que representa o tamanho de uma matriz quadrada. Apresente esta matriz como mostrado na coluna “Resultados”. Observe que as bordas da matriz são feitas por asteriscos (*) e a parte central por símbolos de arroba (@).

tamanho = int(input(""))

for i in range(tamanho):
    for j in range(tamanho):
        if i == 0 or i == tamanho - 1 or j == 0 or j == tamanho - 1:
            print("* ", end="")
        else:
            print("@ ", end="")
    print()
