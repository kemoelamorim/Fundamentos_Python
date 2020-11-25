"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta nescessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
"""
# litros por metro
litro = 1 * 2

# lendo a largura e altura
largura = float(input("Digite a largura em metros: "))
altura = float(input("Digite a altura da parede metros: "))

# calculado área em m²
area = largura * altura

# quantidade de tinta por m²
litros = area/litro

# saída
print('A área da pared é de {:.1f} m², e deve-se usar {:.1f} litros para pinta-la '.format(area, litros))