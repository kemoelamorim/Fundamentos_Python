"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
"""
from math import trunc

# lendo um número
num = float(input("Digite um número: "))

# saída
print(f"Podemos extrair a parte inteira assim: {trunc(num)}.\nOu assim: {int(num)}." )
