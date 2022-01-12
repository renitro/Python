#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
def fat(num):
    if num == 0:
        return 1
    else:
        return num * (fat(num-1))
    

teste = int(input("Digite o numero para descobrir seu fatorial:"))
print(fat(teste))
    