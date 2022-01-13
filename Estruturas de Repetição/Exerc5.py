#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

paisA = int(input("Digite a população do país A: "))
taxaCresA = float(input("Digite a taxa de crescimento do país A: "))
paisB = int(input("Digite a população do país B: "))
taxaCresB = float(input("Digite a taxa de crescimento do país B: "))
cont = 0

if (paisA > paisB):
    print("País A já tem mais habitantes que país B")
elif (taxaCresA < taxaCresB):
    print("Taxa de crescimento do país A é menor que a taxa do país B.")
else:
    while (paisA <= paisB):
        paisA = paisA*taxaCresA
        paisB = paisB*taxaCresB
        cont += 1

print("Demoraram",cont,"anos para a população do país A ultrapassasse a do país B")