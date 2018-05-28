#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um 
# link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando 
# este link (em minutos).

arquivo = float(input("Digite o tamanho do arquivo (em MB): "))
vel_link_net = float(input("Digite a velocidade da sua net (em Mbps): "))

segundos = arquivo/(vel_link_net/8)
minutos = segundos/60

print("Demorará aproximadamente",minutos,"minutos para baixar seu arquivo!")