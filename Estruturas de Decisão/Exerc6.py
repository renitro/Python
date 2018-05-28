#6 - Faça um Programa que leia três números e mostre o maior deles.

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))

if a >= b and a >= c:
    print("\nO maior número digitado é:",a)
elif b >= a and b >= c:
    print("\nO maior número digitado é:",b)
else:
    print("\nO maior número digitado é:",c)