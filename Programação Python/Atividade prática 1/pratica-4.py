# Ler um valor inteiro que representa o mês de uma data e apresentar o trimestre correspondente.

mes_input = int(input())

def formataMes(mes_input):
    if mes_input in [1, 2, 3]:
        return f"{mes_input}, primeiro trimestre"
    elif mes_input in [4, 5, 6]:
        return f"{mes_input}, segundo trimestre"
    elif mes_input in [7, 8, 9]:
        return f"{mes_input}, terceiro trimestre"
    elif mes_input in [10, 11, 12]:
        return f"{mes_input}, quarto trimestre"
    else:
        return f"{mes_input}, mês inválido!!!"

print(formataMes(mes_input))