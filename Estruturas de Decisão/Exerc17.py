#17 - Faça um Programa que peça um número correspondente a um determinado ano e em 
# seguida informe se este ano é ou não bissexto 4/100/400

ano = int(input("Digite o ano pra verificar se é bissexto: "))

if ((ano % 4) != 0):
    print(ano,"não é um ano bissexto.")
elif(ano % 100 == 0):
    if ((ano % 400) == 0):
        print(ano,"é um ano bissexto!")
    else:
        print(ano,"não é um ano bissexto.")
else:
    print(ano,"é um ano bissexto.")
