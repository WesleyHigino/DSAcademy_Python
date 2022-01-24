# função
h = "wesley"

def aluno():
    print(h)

aluno()

# Acessar variavel dentro do escopo da função

def professor():
   global mesa 
mesa ='wesley'

professor()
print(mesa)


a = 3.1+3.5

print(int(a))