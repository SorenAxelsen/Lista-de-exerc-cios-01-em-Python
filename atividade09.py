def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

numero = int(input("Digite um número: "))
resultado = fatorial(numero)
print(f"{numero}! =", end=" ")
for i in range(1, numero + 1):
    if i != numero:
        print(f"{i} *", end=" ")
    else:
        print(f"{i} =", resultado)
