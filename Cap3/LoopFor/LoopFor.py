"""LOOP FOR"""

# Loop em tupla

tp = (1,2,3)
for i in tp:
    print(i)

# Loop em lista

lt = ["wesley", "warley", "weverton", "welington"]
for nome in lt:
    print(nome)

# imprimindo valores no intervalo de 0 e 5

for numero in range(0,5):
    print("%d num"%(numero))

# imprimindo numeros pares de uma lista 

lista1 = [1,2,3,4,5,6,7,8,9,10]
for num in lista1:
    if num % 2 == 0:
        print (num) 


# Listando os números no intervalo entre 0 e 101, com incremento em 2
for i in range(0,20,2): # 2 é o incremento  
    print(i)

# Strings também são sequências
for caracter in 'Python':
    print (caracter)

