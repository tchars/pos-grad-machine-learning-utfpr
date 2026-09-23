# Faça um programa para ler um valor inteiro que representa o tamanho de uma Lista e a seguir atribua para as posiões pares desta lista o valor 0 (zero) e para as posições ímpares o valor 1 (um). Finalizando, mostre os valores da Lista como mostrado na coluna 'Resultados'.

quantidade = int(input())

lista = [0 if i % 2 == 0 else 1 for i in range(quantidade)]

def formatar_lista(lista):
    resultado = "{"
    for i in range(len(lista)):
        resultado += str(lista[i])
        if i < len(lista) - 1:
            resultado += ", "
    resultado += "}"
    return resultado

print(formatar_lista(lista))