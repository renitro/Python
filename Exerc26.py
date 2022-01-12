#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato

total_eleitores = int(input("Digite o número total de eleitores:"))
loop_eleitores = total_eleitores
votos = []

while (loop_eleitores > 0):
    voto = input("Qual o seu candidato? a, b ou c? ")
    votos.append(voto)
    loop_eleitores -=1

contagem = {item:votos.count(item) for item in votos}

print(contagem)