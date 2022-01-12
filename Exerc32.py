#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
#Fatorial de: 5
#5! =  5 . 4 . 3 . 2 . 1 = 120

num = int(input("Digite o número que deseja saber o fatorial: "))
numstring = str(num)+"! = "
temp = num
total = 1

while num > 1:
    numstring += str(num)+" . "
    total*=num 
    num -= 1 
numstring +="1 = "+str(total)

print("Fatorial de: "+str(temp))
print(numstring)
