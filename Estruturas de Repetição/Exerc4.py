#4 - Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento
# de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que
# calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país
#  B, mantidas as taxas de crescimento.

paisA = 80000
taxaCresA = 1.03
paisB = 200000
taxaCresB = 1.015
cont = 0

while (paisA <= paisB):
    paisA = paisA*taxaCresA
    paisB = paisB*taxaCresB
    cont += 1

print("Demoraram",cont,"anos para a população do país A ultrapassasse a do país B")

