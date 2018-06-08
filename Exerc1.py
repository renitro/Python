# 1 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
#pedindo até que o usuário informe um valor válido.

v = 1
while (v == 1):
    num = int(input("Digite uma nota entre 0 e 10: "))

    if num > 10 or num < 0:
        print("Número inválido! Tente novamente!\n")
    else:
        v = 0
