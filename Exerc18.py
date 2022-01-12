#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma 
# dos valores.

qtd = int(input("Digite a quantidade números a digitar: "))
i = 0
lista = []
soma = 0
while (i < qtd):
    n = int(input("Digite o "+str((i+1))+"º número:"))
    soma += n
    lista.append(n)
    i += 1    

maior = max(lista,key=int)
menor = min(lista,key=int)
print("Menor valor:",menor)
print("Maior valor:",maior)
print("Somatório:",soma)