num = int(input("Digite um número: "))

fib_ant = 0
fib_atual = 1

while fib_atual < num:
    fib_prox = fib_ant + fib_atual
    fib_ant = fib_atual
    fib_atual = fib_prox

if fib_atual == num:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")