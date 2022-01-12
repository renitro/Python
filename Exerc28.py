#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

qtde_cds = int(input("Digite a quantidade de cd's:"))
l_cds = qtde_cds
preco_total = 0
while (l_cds > 0):
    preco_total += float(input("Digite o valor desse CD:"))
    l_cds -= 1


print("Total investido:",preco_total)
print("Preço médio por CD:R$",(preco_total/qtde_cds))