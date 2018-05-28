#19 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, 
# dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades,  12 = 1 dezena e 2 unidades 
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

n = int(input("Digite um número menor que 1000: "))

if n <= 999:
    centenas = int(n/100)
    resto = n%100
    dezenas = int(resto/10)
    resto = resto%10
    resultado = '{0} corresponde a {1} {2}, {3} {4}, {5} {6}'


    if centenas == 1 and dezenas == 1 and resto == 1:
        print("\n", resultado.format(n, centenas, 'centena', dezenas,'dezena e', resto, 'unidade.')) 

    elif centenas == 1 and dezenas == 1 and (resto > 1 or resto < 1):
        print("\n", resultado.format(n, centenas, 'centena', dezenas,'dezena e', resto, 'unidades.')) 

    elif centenas == 1 and (dezenas > 1 or dezenas < 1) and resto == 1:
        print("\n", resultado.format(n, centenas, 'centena', dezenas,'dezenas e', resto, 'unidade.')) 

    elif (centenas > 1 or centenas < 1) and dezenas == 1 and resto == 1:
        print("\n", resultado.format(n, centenas, 'centenas', dezenas,'dezena e', resto, 'unidade.')) 
        
    elif centenas == 1 and (dezenas > 1 or dezenas < 1) and (resto > 1 or resto < 1):
        print("\n", resultado.format(n, centenas, 'centena', dezenas,'dezenas e', resto, 'unidades.')) 
    
    elif (centenas > 1 or centenas < 1) and (dezenas > 1 or dezenas < 1) and resto == 1:
        print("\n",resultado.format(n, centenas, 'centena', dezenas,'dezenas e', resto, 'unidade.')) 

    elif (centenas > 1 or centenas < 1) and dezenas == 1 and (resto > 1 or resto < 1):
        print("\n",resultado.format(n, centenas, 'centenas', dezenas,'dezena e', resto, 'unidades.')) 
    else:
        print("\n",resultado.format(n, centenas, 'centenas', dezenas,'dezenas e', resto, 'unidades.')) 
 
else:
    print("\nNúmero digitado inválido!")