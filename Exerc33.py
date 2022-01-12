#Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível

num = int(input("Digite um numero para descobrir se ele é primo: "))
check = num-1
divisible = []

while (check > 1):
    if num % check  == 0:
        divisible.append(check)
        check -= 1
    else:
        check -= 1

if not divisible:
    print("Número primo!") 
    
else:
    print("Número não primo!", num,"é divisível por:")
    for x in divisible:
        print(x)

    
    