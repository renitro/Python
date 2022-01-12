#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
#    Snippet abrir arquivos vazios
#atual = 11
#while (atual < 52):
#    file = "Exerc"+str(atual)+".py"
#
#    open(file, 'a').close()
#    atual = atual + 1



n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if ((n1+1) < n2):
    n1 = n1+1
    while (n1 < n2):
        print(n1)
        n1 = n1+1
elif ((n2+1) < n1):
    n2 = n2+1
    while (n2 < n1):
        print(n2)
        n2 = n2+1
else:
    print("Não há números entre", n1 ,"e", n2)
