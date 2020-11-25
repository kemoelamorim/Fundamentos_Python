"""
Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
# lendo preço
preco = float(input("Digite o preço: "))

# implementando desconto
desconto = preco * 5 /100
novo_preco = preco - desconto

# saída
print("Preço com desconto = %d" % novo_preco)