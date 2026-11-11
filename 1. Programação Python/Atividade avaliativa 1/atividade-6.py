#Faça um programa para ler uma String e apresente todos as palavras desta String. Leve em consideração que entre as palavras existem um, e somente um, caractere espaço. Veja, também, que o ponto final não faz parte da última palavra. Observe o resultado final na coluna “Resultados”.

frase = input()
palavras = frase.split()
palavras[-1] = palavras[-1].rstrip('.')

print(f"Existem {len(palavras)} palavras, são elas: ")
print()

for i, palavra in enumerate(palavras, start=1):
    print(f'{i}a. palavra = {palavra}')