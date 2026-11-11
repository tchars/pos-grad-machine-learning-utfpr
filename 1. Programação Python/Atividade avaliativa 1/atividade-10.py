#Faça um programa para ler um valor inteiro que representa o tamanho (variável “n”) de uma primeira Lista e a seguir leia todos os “n” elementos desta Lista. E, também, construa uma segunda lista onde seus elementos são assim definidos: a) se o elemento da primeira lista for um valor negativo, armazenar na segunda lista o valor -1 (menos um); b) se o elemento da primeira lista for o valor neutro (zero), armazenar na segunda lista o valor 0 (zero); e, c) se o elemento da primeira lista for um valor positivo, armazenar na segunda lista o valor 1 (um). Finalizando, mostre os valores das Listas como mostrado na coluna 'Resultados'.

n_inputs = int(input())
primeira_lista = []
segunda_lista = []

for i in range(n_inputs):
    elemento = int(input())
    primeira_lista.append(elemento)
    
    if elemento < 0:
        segunda_lista.append(-1)
    elif elemento == 0:
        segunda_lista.append(0)
    else:
        segunda_lista.append(1)

def print_lista(lista):
  string_final = "["
  for i in range(len(lista)):
    string_final += str(lista[i])
    if i < len(lista) - 1:
      string_final += ", "
  string_final += "]"
  return string_final

print(print_lista(primeira_lista))
print(print_lista(segunda_lista))