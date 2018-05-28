#9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = (int(input("Digite um número: ")))
n2 = (int(input("Digite outro número: ")))
n3 = (int(input("Digite mais um número: ")))

if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print("\nOs números digitados, em ordem decrescente:",n1,n2,n3)
    else:
        print("\nOs números digitados, em ordem decrescente:",n1,n3,n2)

elif n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        print("\nOs números digitados, em ordem decrescente:",n2,n1,n3)
    else:
        print("\nOs números digitados, em ordem decrescente:",n2,n3,n1)
else:
    if n1 >= n2:
        print("\nOs números digitados, em ordem decrescente:",n3,n1,n2)
    else:
        print("\nOs números digitados, em ordem decrescente:",n3,n2,n1)