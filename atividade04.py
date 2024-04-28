total_pessoas = 7
contador_pessoas_acima_90_kg = 0
soma_idades = 0

for i in range(total_pessoas):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    peso = float(input(f"Digite o peso (em kg) da {i+1}ª pessoa: "))

    if peso > 90:
        contador_pessoas_acima_90_kg += 1
    
    soma_idades += idade

media_idades = soma_idades / total_pessoas

print("Quantidade de pessoas com mais de 90 quilos:", contador_pessoas_acima_90_kg)
print("Média das idades das sete pessoas:", media_idades)
