#11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram 
# para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
# baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

sal_base = float(input("Digite o salário base: R$"))
aumento = 0

if sal_base <= 280:
    aumento = 20
elif sal_base > 280 and sal_base < 700:
    aumento = 15
elif sal_base > 700 and sal_base < 1500:
    aumento = 10
else:
    aumento = 5

print("\nSalário base: R$",sal_base)
print("Percentual de aumento:",aumento,"%.")
print("Valor do aumento: R$",((aumento/100)*sal_base))
print("Salário novo (com aumento): R$", ((1+(aumento/100))*sal_base))
