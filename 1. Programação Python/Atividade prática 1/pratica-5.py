# Dados dois números A e B, faça um programa que calcule a soma de todos os inteiros existentes entre A e B. No caso de A > B, faça a troca dos valores para fazer A < B antes de realizar o processamento.

valor_a = int(input())
valor_b = int(input())

if valor_a > valor_b:
    valor_a, valor_b = valor_b, valor_a

numeros = list(range(valor_a, valor_b + 1))

string_final = ""
for numero in numeros[:-1]:
    string_final += str(numero) + " + "

string_final += str(numeros[-1]) + " = " + str(sum(numeros))

print(string_final) 