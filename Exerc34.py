#Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.

num = int(input("Digite um numero para descobrir os primos até ele: "))
check = num-1
primo = []

while (check > 1):
    if num % check  == 0:
        
        check -= 1
    else:
        primo.append(check)
        check -= 1

print("\n\n")
print(primo)
