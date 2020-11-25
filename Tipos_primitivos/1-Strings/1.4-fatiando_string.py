# Função split()
nome_completo = 'Kemoel Amorim Miranda'
separando = nome_completo.split(' ')  # quebra a string e transforma em uma lista
print(separando)
print(type(separando))  # viu ;)

# metodos de usar o print""
print("Kemoel", "Amorim", "Miranda", sep = '_') # fatiando com sep = ''
print("pulando", "linha", sep = '\n') # pulando linha '\n'

# Método indice (slice)
sobreMim = 'Sou kemoel'
# ..........0123456789....
print(sobreMim[0:])
print(sobreMim[:10])
subString = sobreMim[4:10]  # pega do índice 4 até o índice 10
print(subString)
print(subString[-6:]) # retornando o índice -6 até o fim

# Método find
moeda = 'Moeda=Real '
index = moeda.find('=')
pegandoReal = moeda[index + 1:]  # lendo o índice '=' + 1 até o final
print(pegandoReal)