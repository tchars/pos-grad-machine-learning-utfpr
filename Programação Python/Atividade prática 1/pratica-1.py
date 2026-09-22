# Fazer um programa que leia dois números inteiros e calcule a média aritmética simples destes números imprimindo o resultado com uma casa decimal.
# Por exemplo:
# Input 5, 6
# Media = 5.5

a, b = int(input()), int(input())

media = (a + b) / 2
print(f"Media = {media:.1f}")