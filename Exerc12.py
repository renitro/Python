#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. 

n = int(input("Digite o valor para mostrar a tabuada: "))
for x in range(10):
    print(n, "X", (x+1), "=", (n*(x+1)) )

