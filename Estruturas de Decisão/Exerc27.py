#27 - Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) 
# de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morangos = float(input("Digite os kgs de morangos: "))
if morangos > 5:
    preco_mor = morangos * 2.2
else:
    preco_mor = morangos * 2.5

macas = float(input("Digite os kgs de maçãs: "))

if macas > 5:
    preco_mac = macas * 1.5
else:
    preco_mac = morangos * 1.8

if (preco_mac+preco_mor) > 25 or (morangos+macas) > 8:
    print("\nTotal a pagar: R$",(preco_mor+preco_mac)*0.9, sep='')
else:
    print("\nTotal a pagar: R$",(preco_mor+preco_mac), sep='')



