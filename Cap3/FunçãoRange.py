# A função range nos permite criar uma lista de numeros em um intervalo específico

# range([start],[stop],[step])

#[start] - número que inicia a sequência 
#[stop] - número que encerraa a sequência(não é incluído na sequência)
#[step] - diferença entre cada número da sequencia 


for i in range (50,101,2):
    print(i)

for i in range (3,6):
    print (i)

for i in range (0, -21, -2):
    print(i)

lista = ['Morango', 'banana', 'Abacaxi', 'uva']
lista_tamanho = len(lista) 
for i in range (0, lista_tamanho):
    print(lista[i])

print(type(range(0,3)))    # tipo do objeto (tudo em python é um objeto)