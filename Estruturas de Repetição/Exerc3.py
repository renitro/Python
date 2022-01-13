#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
sala = float(input("Digite o salário: "))
sexo = input("Digite o sexo (M ou F): ")
estCiv = input("Digite o estado civil (s, c, v, d): ")

if len(nome) >= 3:
    print("Nome com mais de 3 caracteres! Válido!")
else:
    print("Nome com menos de 3 caracteres! Inválido!")

if idade >= 0 and idade <= 150:
    print("Idade entre 0 e 150! Válida!")
else:
    print("Idade fora de 0 a 150! Inválida!")

if sala > 0:
    print("Salário maior que zero! Válido!")
else:
    print("Salário menor que zero! Inválida!")

if sexo == 'f' or sexo == 'F' or sexo == 'm' or sexo == 'M':
    print("Sexo M ou F! Válido!")
else:
    print("Sexo não é M ou F! Inválido!")        

if estCiv == 's' or estCiv == 'c' or estCiv == 'v' or estCiv == 'd' or estCiv == 'S' or estCiv == 'C' or estCiv == 'V' or estCiv == 'D':
    print("Estado civil dentro dos padrões! Válido!")
else:
    print("Estado civil fora dos padrões! Inválido!")        
       
       
            
