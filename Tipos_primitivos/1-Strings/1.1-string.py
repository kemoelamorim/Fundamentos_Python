# texto aspas simples e aspas duplas
aspas_simplis = 'permite aspas "duplas" incorporadas'
print(aspas_simplis)
aspas_duplas = "permite aspas 'simples' incorporadas"
print(aspas_duplas)

# texto com quebra de linha tambem conhecida como Doc String (atalho: atlt + shift + A)
menu = '''Texto com quebra de linha sao 
Strings entre aspas triplas podem ocupar várias linhas - 
todos os espaços em branco associados serão incluídos no literal da string.
'''
print(menu)

# para usar um apócope detro da string
aspas_duplas_apocope = "Olho d'água"  # aqui não ha problema
print(aspas_duplas_apocope)

# aqui é nescesário usar \ (barra investida) para ascapar das aspas simples
aspas_simplis_apocope = 'Olho d\'água' 
print(aspas_simplis_apocope)


