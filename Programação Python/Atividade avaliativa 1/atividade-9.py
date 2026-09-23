# Faça um programa para ler um valor inteiro (variável “a”) e a seguir construa uma Lista com 10 (dez) posições (variável “x”) com o resultado da seguinte expressão: x[i] = a + i; para todo “i” variando de 0 até 9.

a = int(input())
x = []

for i in range(10):
    x.append(a + i)
    print(f"x[{i}] = {a} + {i} = {x[i]}")