#3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
# F - Feminino, M - Masculino, Sexo Inválido

sexo = input("Digite seu sexo: (M ou F): ")

if sexo == 'M' or sexo == 'm':
    print("\nM = Masculino!")
elif sexo == 'F' or sexo == 'f':
    print("\nF = Feminino!")
else:
    print("\nSexo Inválido!")