"""
Escreva um programa que leia um valor em metros e o exiba convertido em centimetro e milimetros.
"""
valor = int(input('Digite um valor em metros: '))
centimetros = valor * 100
milimetros = valor * 1000
print('O valor {} convertido para centimetros é {} e para milimetros é {}'.format(valor, centimetros,milimetros))
