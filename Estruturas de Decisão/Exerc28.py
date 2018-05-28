#28 - O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara 
# o cliente receberá ainda um desconto de 5% sobre o total a compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e 
# gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, 
# tipo de pagamento, valor do desconto e valor a pagar.

tipo_car = int(input("Digite qual carne você deseja: (1 para Filé Duplo, 2 para Alcatra e 3 para Picanha): "))
kg_car = float(input("Digite quantos kgs de carne você deseja: "))
cartao = input("Deseja utilizar o Cartão Tabajara?: ").upper()
desconto = 0
preco_tot = 0

if tipo_car == 1:
    if kg_car <= 5:
        preco_tot = kg_car*4.9 
    else:
        preco_tot = kg_car*5.8

    print("\nTipo de carne: Filé Duplo.")
    print("Quantidade de carne: ",kg_car,"kgs.", sep = '')
    print("Valor total: R$",preco_tot, sep = '')
    if cartao == "SIM" or cartao == "S":
        desconto = preco_tot*0.05
        print("Tipo de pagamento: Cartão Tabajara")
        print("Desconto (10%): R$",desconto,sep = '')
        print("Total a pagar: R$",(preco_tot*0.95),sep = '')
    else:
        print("Tipo de pagamento: Dinheiro")
        print("Desconto: R$",desconto,sep = '')
        print("Total a pagar: R$",(preco_tot),sep = '')

elif tipo_car == 2:

    if kg_car <= 5:
        preco_tot = kg_car*5.9 
    else:
        preco_tot = kg_car*6.8

    print("\nTipo de carne: Alcatra.")
    print("Quantidade de carne: ",kg_car,"kgs.", sep = '')
    print("Valor total: R$",preco_tot, sep = '')
    if cartao == "SIM" or cartao == "S":
        desconto = preco_tot*0.05
        print("Tipo de pagamento: Cartão Tabajara")
        print("Desconto (5%): R$",desconto,sep = '')
        print("Total a pagar: R$",(preco_tot*0.95),sep = '')
    else:
        print("Tipo de pagamento: Dinheiro")
        print("Desconto: R$",desconto,sep = '')
        print("Total a pagar: R$",(preco_tot),sep = '')


elif tipo_car == 3:
    if kg_car <= 5:
        preco_tot = kg_car*6.9 
    else:
        preco_tot = kg_car*7.8

    print("\nTipo de carne: Picanha.")
    print("Quantidade de carne: ",kg_car,"kgs.", sep = '')
    print("Valor total: R$",preco_tot, sep = '')
    if cartao == "SIM" or cartao == "S":
        desconto = preco_tot*0.05
        print("Tipo de pagamento: Cartão Tabajara")
        print("Desconto (10%): R$",desconto,sep = '')
        print("Total a pagar: R$",(preco_tot*0.95),sep = '')
    else:
        print("Tipo de pagamento: Dinheiro")
        print("Desconto: R$",desconto,sep = '')
        print("Total a pagar: R$",(preco_tot),sep = '')

else:
    print("\nTipo de carne inválido!")    
