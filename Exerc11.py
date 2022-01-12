#Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = 0
if ((n1+1) < n2):
    m = n1
    M = n2
    n1 = n1+1
    
    while (n1 < n2):
        soma += n1
        print(n1)
        n1 = n1+1
    print("A soma dos números compreendidos entre", m,"e", M,"é", soma )
elif ((n2+1) < n1):
    m = n2
    M = n1
    
    n2 = n2+1
    while (n2 < n1):
        soma += n2
        print(n2)
        n2 = n2+1
    print("A soma dos números compreendidos entre", m,"e", M,"é", soma )
else:
    print("Não há números entre", n1 ,"e", n2)