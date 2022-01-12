#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

def fat(num):
    if num == 0:
        return 1
    else:
        return num * (fat(num-1))

n = 1    

while n > 0:
    n = int(input("Digite o numero para descobrir seu fatorial (0 ou menor sai, 16 ou mais retorna):"))
    if n < 0:
        break
    elif n < 16:
        print(fat(n))
    else: 
        pass 
    