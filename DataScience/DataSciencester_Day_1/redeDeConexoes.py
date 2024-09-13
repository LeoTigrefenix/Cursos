


lista_nomes = [
    {"id":0, "nome":"Zero"},
    {"id":1, "nome":"Um"},
    {"id":2, "nome":"Dois"},
    {"id":3, "nome":"Tres"},
    {"id":4, "nome":"Quatro"},
    {"id":5, "nome":"Cinco"},
    {"id":6, "nome":"Seis"},
    {"id":7, "nome":"Sete"},
    {"id":8, "nome":"Oito"},
    {"id":9, "nome":"Nove"}
]

lista_amizades = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

# criar um termo a mais nos objetos dentro da lista_nomes chamado "amigos"
for pessoa in lista_nomes:
    pessoa["amigos"]= []

print("--------------")
for obj in lista_nomes:
    print(f" {obj} ")
    print("   ")
print("--------------")

#agora preencher o vetor amigos com os dados corretos
# i,j vai ler os valores dentro da lista de amizades como sendo (i,j)
for i,j in lista_amizades:
    lista_nomes[i]["amigos"].append({"id":lista_nomes[j]["id"], "nome":lista_nomes[j]["nome"]}) # o ID j no vetor de amigos de i
    lista_nomes[j]["amigos"].append({"id":lista_nomes[i]["id"], "nome":lista_nomes[i]["nome"]}) # o ID i no vetor de amigos de j

#printar a lista montada com os nomes e id de amigos
print("Pos lista de amizades temos:")
for obj in lista_nomes:
    print(f" {obj} ")
    print("   ")

#conexões por usuário
def numero_de_amigos(entrada):
    return len(entrada["amigos"])

##contar conexões
total_conexoes = sum(numero_de_amigos(pessoa) for pessoa in lista_nomes)
print(f" total_conexoes: {total_conexoes}")


#média do número de conexões
media_conexoes = total_conexoes/len(lista_nomes)
print(f" media_conexoes: {media_conexoes}")


#número de conexões por pessoa
conexao_por_pessoa = [(pessoa["id"], numero_de_amigos(pessoa)) for pessoa in lista_nomes] # da para acessar com conexao_por_pessoa[0] e o mais interno com conexao_por_pessoa[0][1]

conexao_por_pessoa_detalhado = [{"nome":pessoa["nome"],"conexoes": numero_de_amigos(pessoa)} for pessoa in lista_nomes]

print(conexao_por_pessoa)
print("  ")
print(conexao_por_pessoa_detalhado)


# def amigo_do_amigo(usuario):
#     #ada será a abreviação de amigo do amigo
#     return[ada["id"]
#             for amigo in usuario["amigos"]
#             for ada in amigo["amigos"]]