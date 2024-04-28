maior = float('-inf')

print("Digite 5 números de ponto flutuante:")
for i in range(5):
    numero = float(input(f"Número {i+1}: "))
    if numero > maior:
        maior = numero

print("O maior número informado é:", maior)
