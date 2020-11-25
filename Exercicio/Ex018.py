"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import sin, cos, tan, radians
# lendo ângulo
angulo = int(input("Digite o ângulo: "))

# valores de seno e cosseno
seno = sin(radians(angulo))
print("O ângulo de %d tem o seno de %.2f" %(angulo, seno))
cosseno = cos(radians(angulo))
print("O ângulo de %d tem o seno de %.2f" %(angulo, cosseno))
tangente = tan(radians(angulo))
print("O ângulo de %d tem o seno de %.2f" %(angulo, tangente))
