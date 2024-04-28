total_pessoas = 7
contador_mais_90_kg = 0
soma_idades = 0

for _ in range(total_pessoas):
    idade = int(input("Digite a idade da pessoa: "))
    peso = float(input("Digite o peso (em kg) da pessoa: "))

    if peso > 90:
        contador_mais_90_kg += 1
    
    soma_idades += idade

media_idades = soma_idades / total_pessoas

print("Quantidade de pessoas com mais de 90 quilos:", contador_mais_90_kg)
print("Média das idades das sete pessoas:", media_idades)
