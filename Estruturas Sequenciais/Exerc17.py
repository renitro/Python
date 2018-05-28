#17 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, 
# que custam R$ 25,00
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e 
# sempre arredonde os valores para cima, isto é, considere latas cheias.
from math import ceil, floor


quantidade_lata = 18
quantidade_galao = 3.6
rendimento_tinta = 6
galoes = 0
latas = 0

area = float(input("Informe a área a ser pintada: "))
litros_necessarios = (area / rendimento_tinta) * 1.1


total_latas = ceil(litros_necessarios/quantidade_lata)
print("Comprando apenas latas, é necessário",total_latas,"latas, custando R$",(total_latas*80))

total_galao = ceil(litros_necessarios/quantidade_galao)
print("Comprando apenas galões, é necessário",total_galao,"galões, custando R$",(total_galao*25))

latas = floor(litros_necessarios/quantidade_lata)

print ("Misturando, são necessárias",latas,"latas, custando R$",(latas*80))

litros_restantes = litros_necessarios - (latas)*18

galoes = ceil(litros_restantes/quantidade_galao)

print ("E são necessários",galoes,"galões, custando R$",(galoes*25))

