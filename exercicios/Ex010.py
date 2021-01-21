"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
"""
carteira = float(input('Quanto tem na carteira? '))
compra = carteira / 5.78  # Ex. do valor do Dólar 
print('Você tem R$ {:.2f} e pode comprar US$ {:.2f} '.format(carteira, compra))
