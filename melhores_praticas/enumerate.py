"""
Você pode usar enumerate()em um loop quase da mesma maneira que usa o objeto iterável original. Em vez de colocar o iterável diretamente após inno for loop, coloque-o entre parênteses de enumerate()
"""


nome = "kemoel"
for count, value in enumerate(nome):
    print(count, value)


""" 
Neste exemplo, você passa start=1, que começa countcom o valor 1 na primeira iteração do loop. Compare isso com os exemplos anteriores, nos quais start tinha o valor padrão de 0, e veja se você consegue detectar a diferença.
"""

nome = "kemoel"
for count, value in enumerate(nome, start=1):
    print(count, value)
