#18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input("Digite uma data com o seguinte formato dd/mm/aaaa: ")
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

validade = "true"

if (ano%4 == 0 and ano%100!= 0) or ano%400 == 0:
    bissexto = "sim"
else:
    bissexto = "nao"

if mes < 1 or mes > 12:
    validade = "false"

if dia > 31 or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30):
    validade = "false"

if (mes == 2 and bissexto == "nao" and dia > 28) or ( mes == 2 and bissexto == "sim" and dia > 29):
    validade = "false"


if validade == "true":
    print("\nData Válida!")
else:
    print("\nData Inválida!")
