#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

def fib(num):
    if num == 0:
        return 0
    elif num <= 2:
        return 1
    
    return fib(num - 1) + fib(num - 2)


for x in range(16):
    print(fib(x))