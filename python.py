generos = ['policial', 'indefinido', 'terror', 'suspense', 'amor']
#troca o ultimo elemento
generos[-2] = 'ação'
#adiciona um elemento ao fim
generos.append('romantico')
generos.append('drama')
#remove um elemento
generos.remove('terror')
#imprime numerado
for i, prog in enumerate(generos):
    print (i+1, '-->', prog)
print (generos)