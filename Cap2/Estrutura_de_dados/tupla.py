# Tupla

# Tuplas são imutáveis diferente do list, o que significa que não podem ser alteradas, se usa tuplas 
# em dados que não precisam ser alterados como dias da semana ou datas em um calendário.

# Sintaxe : tupla = ("item1", item2, ...)

tupla = ("24/05/2022","semana 3", "dia 24")
print(tupla[1])
print(tupla[0])

#tupla[2] = "dia 25" # não é possivel alterar uma tupla
print(tupla[2])

lista = list(tupla) # Um jeito de alterar a tupla é transformando ela para uma lista para alterar
lista[2] = "dia 21" # o valor e depois transformar para tupla novamente.
lista.append("mes 5")
tupla = lista
print(tupla)


