#13 - Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
# se digitar outro valor deve aparecer valor inválido.

dia = int(input("Digite um número correspondente a um dia da semana (1-7): "))

if dia < 1 or dia > 7:
    print("\nDia digitado inválido! Apenas valores de 1 a 7.")
elif dia == 1:
    print("\nDia digitado: Domingo!")
elif dia == 2:
    print("\nDia digitado: Segunda!")
elif dia == 3:
    print("\nDia digitado: Terça!")
elif dia == 4:
    print("\nDia digitado: Quarta!")
elif dia == 5:
    print("\nDia digitado: Quinta!")
elif dia == 6:
    print("\nDia digitado: Sexta!")
elif dia == 7:
    print("\nDia digitado: Sábado!")