# É preciso tomar cuidado com a com a idntação

""""" CONDICIONAL IF, ELSE """""

if 5 > 1:
    print("cinco maior do que 1")

#-----------

if 10 >11:
    print("maior q 11")
else:
    print("menor que 11") 

#-----------

print(5>2) # verdadeiro ou falso
print(2>5)

#------------

if 5 == 5 :         # Espera um resultado booleano
    print("igual")

if 5 == 6:
    print("igual")  # sera um resultado falso

# Atenção com a sintaxe (ERRO)
#if 4 > 3  # Esta faltado os dois pontos
#    print("Tudo funciona!")

# Atenção com a sintaxe (ERRO)
#if 4 > 3:
#print("Tudo funciona!")  # Sem identação



""" CONDICIONAL ANINHADO """

idade = 18
if (idade == 18):
    print("maior de idade")

#-----------

nome = 'wesley'
if (idade > 17):
    print(nome + ", maior de idade")
else:
    print(nome + ", menor de idade")

#------aninhada-------

nome2 = "cleber"
if (idade == 18 ):
    if (nome2 == "cleber"):
       print("cliente correto")
    else:
        print("cliente incorreto")

#-------------

idade = 13
Nome = "maria"
if (idade >= 14) or (Nome == "maria"):
    print("maria tem permicao para entrar!")


""" CONDICIONAL ELIF"""

# O elif evita a estrtura de varios itens alinhados 

dia = "terça"
if (dia == "segunda"):
    print("hoje é segunda")
else:
    print("hoje é terça")

#--------------

if (dia == 'segunda'):
    print("segunda feira")
elif (dia == "terça"):
    print("terça feira")
else:
    print("outros dias")


""" OPERADORES LOGICOS """    

idade = 18
if idade > 17 and nome == "Bob":
    print("Autorizado!")


#-----------

# Usando mais de uma condição na cláusula if 

disciplina = input('Digite o nome da disciplina: ')            # função input para Entrada de dados 
nota_final = input('Digite a nota final (entre 0 e 100): ')

if disciplina == 'Geografia' and nota_final >= '70':
    print('Você foi aprovado!')
else:
    print('Lamento, acho que você precisa estudar mais!')


# Usando mais de uma condição na cláusula if e introduzindo Placeholders

disciplina = input('Digite o nome da disciplina: ')
nota_final = input('Digite a nota final (entre 0 e 100): ')
semestre = input('Digite o semestre (1 a 4): ')

if disciplina == 'Geografia' and nota_final >= '50' and int(semestre) != 1:
    print('Você foi aprovado em %s com média final %r!' %(disciplina, nota_final)) # O %r deixa a string com aspas ''.
else:
    print('Lamento, acho que você precisa estudar mais!')