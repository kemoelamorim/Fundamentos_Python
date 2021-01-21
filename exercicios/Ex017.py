"""
Faça um programa que leia o comprimento do cateto oposto e di cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.
"""
from math import hypot
# lendo catetos
cateto_oposto = float(input("Digite o cateto oposto: "))
cateto_adjacente = float(input("Digite o cateto adjacente: "))

# calculando hipotenusa
hipotenusa = hypot(cateto_oposto,cateto_adjacente)

# saída
print(f"O comprimento da hipotenusa é {hipotenusa}")