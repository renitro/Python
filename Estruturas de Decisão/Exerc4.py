#4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")

if (letra == 'A' or letra == 'a') or (letra == 'E' or letra == 'e') or (letra == 'I' or letra == 'i') or (letra == 'O' or letra == 'o') or (letra == 'U' or letra == 'u'):
    print("\nA letra digitada é uma vogal!")
else:
    print("\nA letra digitada é uma consoante!")