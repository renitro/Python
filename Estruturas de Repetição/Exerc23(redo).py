#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

num = int(input("Digite um numero para descobrir se ele é primo: "))
check = num-1
primos = []
cont = 0
while (check > 1):
    if num % check  == 0:
        check -= 1
        cont += 1
    else:
        primos.append(check)
        check -= 1
        cont += 1

print("Números primos de 1 a", num,":")
for x in primos:
    print(x)
