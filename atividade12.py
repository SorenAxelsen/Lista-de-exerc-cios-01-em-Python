total_pessoas = 25
quantidade_acima_50_anos = 0
soma_alturas_10_20_anos = 0
quantidade_peso_menor_40 = 0
total_pessoas_analisadas = 0

for _ in range(total_pessoas):
    idade = int(input("Digite a idade da pessoa: "))
    altura = float(input("Digite a altura (em metros) da pessoa: "))
    peso = float(input("Digite o peso (em kg) da pessoa: "))
    
    if idade > 50:
        quantidade_acima_50_anos += 1
    
    
    if 10 <= idade <= 20:
        soma_alturas_10_20_anos += altura
    
    
    if peso < 40:
        quantidade_peso_menor_40 += 1
    
    
    total_pessoas_analisadas += 1


media_alturas_10_20_anos = soma_alturas_10_20_anos / total_pessoas_analisadas


porcentagem_peso_menor_40 = (quantidade_peso_menor_40 / total_pessoas_analisadas) * 100


print("a) Quantidade de pessoas com idade superior a 50 anos:", quantidade_acima_50_anos)
print("b) Média das alturas das pessoas com idade entre 10 e 20 anos:", media_alturas_10_20_anos)
print("c) Porcentagem de pessoas com peso inferior a 40 quilos entre todas as analisadas:", porcentagem_peso_menor_40, "%")
