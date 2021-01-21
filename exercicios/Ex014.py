"""
Faça um programa que converta uma temperatura ditigada em °C (Celsius)e converta para °F(Fahrenheit).
"""
# lendo em C
celsius = float(input("Digite a temperatuda em °C: "))

#  convertendo para fahrenheit
fahrenheit = (celsius * 1.8) + 32

# saída
print("A temperatura em fahrenheit é %d °F" %fahrenheit)