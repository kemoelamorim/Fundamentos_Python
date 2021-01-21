""" 
Neste exemplo, você passa start=1, que começa countcom o valor 1 na primeira iteração do loop. Compare isso com os exemplos anteriores, nos quais start tinha o valor padrão de 0, e veja se você consegue detectar a diferença.
"""

nome = "kemoel"
for count, value in enumerate(nome, start=1):
    print(count, value)
