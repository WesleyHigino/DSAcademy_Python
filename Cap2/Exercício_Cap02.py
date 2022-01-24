# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.

from itertools import count


lista1 = [1,2,3,4,5,6,7,8,9,10]
print(lista1)
print(lista1[0])
print(lista1[1])
print(lista1[2])
print(lista1[3])
print(lista1[4])
print(lista1[5])
print(lista1[6])
print(lista1[7])
print(lista1[8])
print(lista1[9])

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela

lista2 = ["caneta", "lapis","borracha","apontador", "marca texto"]
print(lista2)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string

nome = "wesley"
sobrenome = "higino"
print(nome+" "+sobrenome)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla

linha = (1,2,2,3,4,4,4,5)
print(linha.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela

dicionario1 = {}
print(dicionario1)
dicionario1 = "matematica", "2f"
print(dicionario1)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela

dicionario2 = {"graduacao1" :"engenharia", "graduacao2":"medicina", "graduacao3":"jornalismo"}
print(dicionario2["graduacao1"])
print(dicionario2["graduacao2"])
print(dicionario2["graduacao3"])

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela

dicionario2["graduacao4"] = "pedagogia"
print(dicionario2.items())

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.

dicionario3 = {"fiat":"uno", "honda":"civc", "precoCorola": [80.000, 90.000]}
print(dicionario3)
print(dicionario3["precoCorola"][0])
print(dicionario3["precoCorola"][1])

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.

lista3 = ["wesley", ("Mineiro","Brasileiro"), {"idade":"23", "cor":"preta"}, 5100.77]
print(lista3)
print(lista3[0])
print(lista3[1][0])
print(lista3[1][1])
print(lista3[2]["idade"])
print(lista3[2]["cor"])
print(lista3[3])

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
# frase -> Cientista de Dados é o profissional mais esforçado do século XXI kk

frase = 'Cientista de Dados é o profissional mais esforçado do século XXI kk'
print(frase[0:18])