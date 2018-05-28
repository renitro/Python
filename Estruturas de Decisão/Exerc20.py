#20 - Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média 
# alcançada por aluno e presentar:
# A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# A mensagem "Aprovado com Distinção", se a média for igual a 10.

n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))
n3 = float(input("Digite a terceira nota do aluno: "))

media = (n1+n2+n3)/3

if (media <= 7):
    print("\nMédia: " ,media, ". Reprovado!",sep='')
elif(media > 7 and media < 10):
    print("\nMédia: " ,media, ". Aprovado!",sep='')
elif(media == 10):
    print("\nMédia:" ,media, ". Aprovado com Distinção!",sep='')
else:
    print("\nNotas inválidas!")