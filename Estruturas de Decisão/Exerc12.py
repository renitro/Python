#12 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de 
# Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS 
# corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido 
# corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora 
# e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o 
# exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.


val_hora = float(input("Digite o valor de cada hora trabalhada: R$"))
qtde_hora = float(input("Digite a quantidade de horas trabalhadas no mês: "))

sal_bruto = val_hora * qtde_hora

desconto_ir = 0

if sal_bruto <= 900:
    desconto_ir = 0
elif sal_bruto <= 1500: 
    desconto_ir = 5
elif sal_bruto <= 2500:
    desconto_ir = 10
else:
    desconto_ir = 20

valor_desc_ir = desconto_ir/100
FGTS = sal_bruto * 0.11
INSS = sal_bruto * 0.1
totaldescontos = (sal_bruto*valor_desc_ir) + (INSS)

print("\nSalário Bruto: (",val_hora,"*",qtde_hora,"): R$",sal_bruto)
print("(-) IR (",desconto_ir,"%): R$",(sal_bruto*valor_desc_ir))
print("(-) INSS (10%): R$",INSS)
print("FGTS (11%): R$",FGTS)
print("Total de descontos: R$",totaldescontos)
print("Salário Líquido: R$", sal_bruto-totaldescontos)
