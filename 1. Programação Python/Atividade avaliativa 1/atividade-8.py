# Faça um programa para ler do teclado 7 (sete) valores inteiros e os armazene em uma Lista. Em seguida, deverão ser mostrados na tela do computador: todos os elementos da Lista e os menor e maior elementos desta Lista com as suas respectivas posições.

input_list = []

for i in range(7):  
    value = int(input())
    input_list.append(value)

for i in range(len(input_list)):
    print(f"x[{i}] = {input_list[i]}")

print()
print(f"Menor elemento, x[{input_list.index(min(input_list))}] = {min(input_list)}")
print(f"Maior elemento, x[{input_list.index(max(input_list))}] = {max(input_list)}")