#8 - Faça um programa que pergunte o preço de três produtos e informe qual produto 
# você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input("Digite o valor do primeiro produto: "))
p2 = float(input("Digite o valor do segundo produto: "))
p3 = float(input("Digite o valor do terceiro produto: "))

if p1 <= p2 and p1 <= p3:
    print("\nO produto mais barato é o primeiro, com preço: R$",p1)
elif p2 <= p1 and p2 <= p3:
    print("\nO produto mais barato é o segundo, com preço: R$",p2)
else:
    print("\nO produto mais barato é o terceiro, com preço: R$",p3)