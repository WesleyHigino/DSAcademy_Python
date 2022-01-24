# Dicionario

# Os dicionarios de dados são muito utilizados em deep learning 

# Sintaxe : dici = {k1:v1, k2:v2, ...}


""" CHAVE : VALOR"""


dicionario = {
    "curso":"curso de python",
    "Nome completo": "wesley higino",
}

dicionario_salario = {
     "walter" : 2450.00,
     "wesley" : 3500.00
}

dicionario_2 = {
    "curso" : "curso de java",
    "Nome completo" : "eduardo"
}



print("valor : "+dicionario["curso"])
print("valor : "+dicionario["Nome completo"])
print("salario : " +str(dicionario_salario["walter"]))

print(dicionario.keys())   # mostra as chaves do dicionario
print(dicionario.values()) # mostra os valores 
print(dicionario.items())  # mostra os itens que são a combinação de chave e valores 

dicionario.update(dicionario_2) # concatena os dois dicionarios 

dici = {}
dici["carro"] = "celta"  # Adicionando chave e valor em um dicionario vazio
print(dici)


# Os dicionarios de dados são muito utilizados em deep learning 