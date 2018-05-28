#23 - Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
# Dica: utilize uma função de arredondamento.

n = float(input("Digite um numero qualquer: "))

if int(n) == n:
    print("\nNúmero Inteiro!")
else:
    print("\nNúmero Decimal!")
