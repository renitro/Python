#Faça um programa que leia 5 números e informe a soma e a média dos números.

listnum = []
soma = 0
for x in range(5):
    num = input("Digite o "+str(x+1)+"º numero:")
    soma += int(num)
    listnum.append(num)
    

print("A soma dos numeros digitados é:", soma)
print("A media dos numeros digitados é:", (soma/5))