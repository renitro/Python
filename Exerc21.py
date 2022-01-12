#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input("Digite um numero para descobrir se ele é primo: "))
check = num-1
while (check > 1):
    if num % check  == 0:
        check = -1
        break
    else:
        check -= 1
if (check == -1):
    print("Número não primo!")
else:
    print("Número primo!") 