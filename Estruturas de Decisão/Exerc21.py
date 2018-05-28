#21 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e 
# depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 
# 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve
#  se preocupar com a quantidade de notas existentes na máquina.Exemplo 1: Para sacar a quantia de 256 
# reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
# uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

dinheiro = int(input("Digite o valor que deseja sacar: R$"))

n100 = int(dinheiro/100)
dinheiro = dinheiro % 100
n50 = int(dinheiro/50)
dinheiro = dinheiro % 50
n10 = int(dinheiro/10)
dinheiro = dinheiro % 10
n5 = int(dinheiro/5)
n1 = dinheiro %5

resultado = '\nSerão necessárias: {0} notas de R$100, {1} notas de R$50, {2} notas de R$10, {3} notas de R$5 e {4} notas de R$1'

print(resultado.format(n100,n50,n10,n5,n1))


