#24 - Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja 
# realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar; positivo ou negativo; inteiro ou decimal.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
op = input("Digite a operação a realizar: " )

if op == '*' or op == '+' or op == '/' or op == '-':
    if op == '*':
        resultado = (n1*n2)
        print("\n",n1," * ",n2," = ",resultado,".", sep='')

    elif op == '+':
        resultado = (n1+n2)
        print("\n",n1," + ",n2," = ",resultado,".", sep='')   

    elif op == '-':
        resultado = (n1-n2)
        print("\n",n1," - ",n2," = ",resultado,".", sep='')   

    elif op == '/':
        resultado = (n1/n2)
        print("\n",n1," / ",n2," = ",resultado,".", sep='')   

    if resultado %2 == 0:
        print("Número par!")
    else:
        print("Número ímpar!")

    if int(resultado) == resultado:
        print("Número inteiro!")
    else:
        print("Número decimal!")

    if resultado >= 0:
        print("Número positivo!")
    else:
        print("Número negativo!")
else:
    print("\nOperador inválido! Utilize +, -, * e /")