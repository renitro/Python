#25 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

p1 = input("Telefonou para a vítima? Responda sim ou não: ")
p2 = input("Esteve no local do crime?: ")
p3 = input("Mora perto da vítima?: ")
p4 = input("Devia para a vítima?: ")
p5 = input("Já trabalhou com a vítima?: ")

p1 = p1.upper()
p2 = p2.upper()
p3 = p3.upper()
p4 = p4.upper()
p5 = p5.upper()

result = 0
if p1 == "SIM":
    result += 1

if p2 == "SIM":
    result += 1

if p3 == "SIM":
    result += 1

if p4 == "SIM":
    result += 1

if p5 == "SIM":
    result += 1

if result == 5:
    print("\nVocê é o Assassino!")
elif result == 3 or result == 4 :
    print("\nVocê é o Cúmplice!!")
elif result == 2:
    print("\nVocê é Suspeito!")
else:
    print("\nVocê é Inocente!")
