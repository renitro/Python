#10 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou 
# V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
#  "Valor Inválido!", conforme o caso.

turno = input("Digite o turno que você estuda(M-atutino, V-espertino ou N-oturno): ")

if turno == 'V' or turno == 'v':
    print("\nBoa Tarde!")
elif turno == 'N' or turno == 'n':
    print("\nBoa Noite!")
elif turno == 'M' or turno == 'm':
    print("\nBom Dia!")
else:
    print("\nValor Inválido!")