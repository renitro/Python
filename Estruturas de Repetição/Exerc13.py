#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = int(input("Digite a base: "))
exp = int(input("Digite o expoente: "))
total = base
if (exp == 0):
    total = 1

while (exp > 1):
    total = total * base
    exp = exp-1
print(total)