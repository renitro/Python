#26 - Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool: até 20 litros, desconto de 3% por litro, acima de 20 litros, desconto de 5% por litro
# Gasolina: até 20 litros, desconto de 4% por litro, acima de 20 litros, desconto de 6% por litro 
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da 
# seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente 
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

p_gas = 2.5
p_alc = 1.9


comb = input("Digite o tipo de combustível (A para Álcool, G para Gasolina): ").upper()
litros = float(input("Digite a quantidade de litros a abastecer: "))

if comb == 'A':
    if litros <= 20:
        print("\nTotal a pagar: R$",((litros*p_alc)*0.97),sep='')
    else:
        print("\nTotal a pagar: R$",((litros*p_alc)*0.95),sep='')
elif comb == 'G':
    if litros <= 20:
        print("\nTotal a pagar: R$",((litros*p_gas)*0.96),sep='')
    else:
        print("\nTotal a pagar: R$",((litros*p_gas)*0.94),sep='')
else:
    print("\nCombustível inválido!")
