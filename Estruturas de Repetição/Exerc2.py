#2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
#mostrando uma mensagem de erro e voltando a pedir as informações.

v = 1
while (v == 1):
    user = input("Digite o usuário: ")
    passw = input ("Digite a senha: ")

    if (user == passw):
        print("\nUsuário não pode ser igual a senha! Tente novamente!\n")
    else:
        v = 0
