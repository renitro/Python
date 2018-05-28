#16 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades 
# de latas de tinta a serem compradas e o preço total.
import math as m

area = eval(input("Digite a área a ser pintada (em m²): "))

qtdeLatas = m.ceil(area/54)
preco = qtdeLatas*80

print("A quantidade de latas necessarias para pintar",area,"m²: ",qtdeLatas)
print("Preço total: R$",preco)

