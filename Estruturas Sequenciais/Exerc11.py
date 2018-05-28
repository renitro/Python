#11- Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

int1 = (eval(input("Digite um número inteiro: ")))
int2 = (eval(input("Digite outro número inteiro: ")))
real = (eval(input("Digite um número real: ")))

a = (int1 * 2) * (int2 / 2)
b = (int1*3)+real
c = real**3

print("O produto do dobro de",int1,"com a metade de",int2,"é: ",a)
print("A soma do triplo de",int1,"com",real,"é",b)
print(real,"elevado ao cubo é: ",c)