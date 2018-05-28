#6 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. Area = pi * area²
import math as m

raio = eval(input("Digite o raio do circulo: "))

area = m.pi*(raio**2)

print("A área do círculo é: ",area)