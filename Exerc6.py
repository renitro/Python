#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro

linha = ""
for x in range(21): 
    linha += str(x) + " "
    print(x)

print("\n\n"+linha)