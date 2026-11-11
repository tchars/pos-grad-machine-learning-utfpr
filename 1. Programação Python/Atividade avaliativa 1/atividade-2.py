# Faça um programa que leia um valor inteiro do teclado (variável “item”) e a seguir implemente a rotina de busca sequencial: do primeiro elemento da Lista até encontrar; ou até o final da Lista e não encontrar. Mostre as posições juntas dos respectivos elementos da Lista “a” e, finalizando, com o resultado da busca: encontrou na posição tal; ou não encontrou “item” na Lista “a”. Observe o resultado final na coluna “Resultados”.

lista = {0:10, 1:2, 2:7, 3:8, 4:5, 5:3, 6:22, 7:17, 8:18}

busca = int(input(""))
resultado = False
posicao = 0

for i in range(len(lista)):
  if lista[i] == busca:
    posicao = i
    resultado = True
    break

def print_lista(lista):
  string_final = "{"
  
  for i in range(len(lista)):
    string_final += f"{i}:{lista[i]}, "
  
  string_final = string_final[:-2] + "}"
  
  print(string_final)
  print()


print_lista(lista)

if resultado:
  print("Item: {}, foi encontrado na posicao {}.".format(busca, posicao))
else:
  print("Item: {}, \"nao\" foi encontrado.".format(busca))