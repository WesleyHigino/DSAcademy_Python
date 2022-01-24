nomes = ["wesley","warley","wanderson","weverton"]

print(nomes)
print(nomes[1])
print(nomes[0:3])
print(nomes [-1])

nomes[2] = "adilson"
print(nomes)

""" adicionando elementos"""

nomes.append ("elizete")
nomes.append ("warley")
print(nomes)

"""Len indica a quantidade de elementos dentro do Array"""

print(str(len(nomes))+ " membros da familia")

""" Removver elementos """

nomes.remove("wesley")
print(nomes)

"""Remove o ultimo elemento"""

nomes.pop()
print(nomes)

"""Remover pela posição dos elementos"""

del nomes[2]
print(nomes)

"""copiar list"""

nomes2=list(nomes)
print(nomes2)

# list aninhada, listas dentro de outras listas

listaaninhada = [[1,2,3], [4,5,6], [7,8,9]]
print(listaaninhada[0])
print(listaaninhada[1])
print(listaaninhada[2])

"""Acessando lista das listas"""
a = listaaninhada[0]
b = listaaninhada[1] 
c = listaaninhada[2] 

print(a[0])
print(a[1])
print(a[2])

"""ou através do conceitos de matriz"""

print(listaaninhada[1][2])
print(listaaninhada[0][1])
print(listaaninhada[2][0])
print(listaaninhada[2][0] + 10)

# Adicionando elemento na lista
listaaninhada.append([5,7,10])
print(listaaninhada)

# Add elemento na lista dentro da lista 
a.append(11)
print(listaaninhada)

# utilizando operador IN
print(2 in a)
print(8 in listaaninhada[2])
print(10 in listaaninhada[1])