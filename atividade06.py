soma_pares = 0
soma_impares = 0
soma_divisiveis_por_3 = 0


for _ in range(10):
    numero = int(input("Digite um número: "))
    
    
    if numero % 2 == 0:
        soma_pares += numero
    else:
        soma_impares += numero
    
    if numero % 3 == 0:
        soma_divisiveis_por_3 += numero


print("Soma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)
print("Soma dos números divisíveis por 3:", soma_divisiveis_por_3)
