#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

def fib(num):
    if num == 0:
        return 0
    elif num <= 2:
        return 1
    
    return fib(num - 1) + fib(num - 2)

n = int(input("Digite quantos números de Fibonacci você deseja:"))
for x in range(n):
    print(fib(x))

