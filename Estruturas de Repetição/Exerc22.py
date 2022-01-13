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

    
    