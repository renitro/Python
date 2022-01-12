#Faça um programa que leia 5 números e informe o maior número
num = []
for x in range(5):
    num.append(input("Digite o "+str(x+1)+"º numero:"))

maior_num = max(num, key=int)
print("O maior numero digitado é: "+ maior_num)