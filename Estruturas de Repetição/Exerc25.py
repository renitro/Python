#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

qtd = int(input("Quantas pessoas estão na turma? "))
idade = 0
media = 0
tmp = qtd
while (tmp >0):
    idade = int(input("Qual a sua idade? "))
    media +=idade
    tmp -=1

media = media/qtd     
if media <= 25:
    print("A turma é jovem!")
elif media <= 60:
    print("A turma é adulta!")
else:
    print("A turma é idosa!")
    