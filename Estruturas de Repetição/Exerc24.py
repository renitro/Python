#Faça um programa que calcule o mostre a média aritmética de N notas.

nota  = 0
notas = []
total = 0
while (nota >= 0):
    nota = float(input("Digite a nota do aluno (menor que zero sai e mostra resultado): "))
    if nota < 0:
        break
    else:
        notas.append(nota)
        total += nota
print("Media aritmética de todas as notas:(Total dividido por",len(notas),"):")
print(total/len(notas))