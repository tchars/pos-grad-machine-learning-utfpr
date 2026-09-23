#Faça um programa para ler uma String e apresente todos os caracteres desta String 3 (três) vezes na tela do computador. Observe o resultado final na coluna “Resultados”.

texto = input()

for i in range(3):
    for caractere in texto:
        print(f"{caractere} ", end="")
    print()