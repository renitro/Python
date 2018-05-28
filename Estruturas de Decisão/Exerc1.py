#1 - Faça um Programa que peça dois números e imprima o maior deles.

n1 = (int(input("Digite um número: ")))
n2 = (int(input("Digite outro número: ")))

if n1 > n2:
    print("\n",n1,"é o maior número digitado.")
elif n2 > n1:
    print("\n",n2,"é o maior número digitado.")
else:
    print("\nOs números digitados são iguais. (",n1,",",n2,").")