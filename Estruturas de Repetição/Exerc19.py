#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
qtd = 0
while qtd > 1000 or qtd < 1:
    qtd = int(input("Digite a quantidade números a digitar: "))
i = 0
lista = []
soma = 0
while (i < qtd):
    n = 0
    while n > 1000 or n < 1:
        n = int(input("Digite o "+str((i+1))+"º número:"))
    soma += n
    lista.append(n)
    i += 1    

maior = max(lista,key=int)
menor = min(lista,key=int)
print("Menor valor:",menor)
print("Maior valor:",maior)
print("Somatório:",soma)