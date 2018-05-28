#20 - Fazer um algoritmo que obtenha o raio e a altura de um cilindro e que calcule e escreva sua área e seu volume.
#Área = 2*π*raio*(altura+raio) e Volume = π*raio2*altura.
import math 


raio = eval(input("Digite o raio do cilindro (em cm): "))
altura = eval(input("Digite a altura do cilindro (em cm): "))

area = (2*(math.pi)*raio*(altura+raio))
volume = (math.pi)*raio**2*altura


print("A area do cilindro eh: {0}cm²\nO volume do cilindro eh: {1}cm³".format(area,volume))




