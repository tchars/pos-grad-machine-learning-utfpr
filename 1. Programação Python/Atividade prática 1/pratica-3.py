#Faça um programa que calcule a média aritmética simples de um aluno, a partir de suas 3 notas obtidas no curso. Mostre, ao final, a mensagem: "A MEDIA FINAL FOI ..." . Informar também se o aluno foi aprovado, mostrando a mensagem "APROVADO" caso a média final seja maior ou igual a 7; "RECUPERAÇÃO" caso a média final esteja no intervalo de 5 até 7 e "REPROVADO" caso a média final seja menor que 5.

primeira_nota, segunda_nota, terceira_nota = float(input()), float(input()), float(input())

media_final = (primeira_nota + segunda_nota + terceira_nota) / 3
resultado = ""

if media_final >= 7:
    resultado = "{APROVADO}"
elif 5 <= media_final < 7:
    resultado = "{RECUPERAÇÃO}"
else:
    resultado = "{REPROVADO}"

print(f'A MEDIA FINAL FOI {media_final:.2f} {resultado}')