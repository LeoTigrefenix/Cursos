
# ==============================================================================================
#DECLARAÇÕES
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
# ==============================================================================================
# ==============================================================================================
# criar um termo a mais nos objetos dentro da lista_nomes chamado "amigos"
for pessoa in lista_nomes:
    pessoa["amigos"]= []
# print("--------------")
# for obj in lista_nomes:
#     print(f" {obj} ")
#     print("   ")
# print("--------------")
# ==============================================================================================
# ==============================================================================================
#agora preencher o vetor amigos com os dados corretos
# i,j vai ler os valores dentro da lista de amizades como sendo (i,j)
for i,j in lista_amizades:
    lista_nomes[i]["amigos"].append({"id":lista_nomes[j]["id"], "nome":lista_nomes[j]["nome"]}) # o ID j no vetor de amigos de i
    lista_nomes[j]["amigos"].append({"id":lista_nomes[i]["id"], "nome":lista_nomes[i]["nome"]}) # o ID i no vetor de amigos de j


#o fato de ter montado na linha 31 um sistema sem a lista de amigos em casa amigo eu preciso pegar o id 
##da pessoa e ai ir na lista ver os akigos dela 

#printar a lista montada com os nomes e id de amigos
# print("Pos lista de amizades temos:")
# for obj in lista_nomes:
#     print(f" {obj} ")
#     print("   ")
# ==============================================================================================
# ==============================================================================================
#conexões por usuário
def numero_de_amigos(entrada):
    return len(entrada["amigos"])

##contar conexões
total_conexoes = sum(numero_de_amigos(pessoa) for pessoa in lista_nomes)
#LOG
# print(f" total_conexoes: {total_conexoes}")


#média do número de conexões
media_conexoes = total_conexoes/len(lista_nomes)
#LOG
# print(f" media_conexoes: {media_conexoes}")


#número de conexões por pessoa
conexao_por_pessoa = [(pessoa["id"], numero_de_amigos(pessoa)) for pessoa in lista_nomes] # da para acessar com conexao_por_pessoa[0] e o mais interno com conexao_por_pessoa[0][1]

conexao_por_pessoa_detalhado = [{"nome":pessoa["nome"],"conexoes": numero_de_amigos(pessoa)} for pessoa in lista_nomes]
#LOG
# print(conexao_por_pessoa)
# print("  ")
# print(conexao_por_pessoa_detalhado)
# print(" ------------------------------ ")
# ==============================================================================================
# ==============================================================================================
# amigo de amigo , vai devoltar uma lista dos amigos dos amigos de cada id
def amigo_de_amigo(usuario):
    vetorvazio = []
    for amigos in usuario["amigos"]:
        print(f"amigos {amigos}")
        print(lista_nomes[amigos["id"]])
        for x in lista_nomes[amigos["id"]]["amigos"]:
            print(f"amigoAmigoDados {x}")
            vetorvazio.append(x)

    return {"id":usuario["id"],"amigos_de_amigos":vetorvazio}

tentativa = {'id': 0, 'nome': 'Zero', "amigos":[{'id': 1, 'nome': 'Um'},{'id': 2, 'nome': 'Dois'}]}
print(f"Teste primeiro {amigo_de_amigo(tentativa)}")
# ==============================================================================================
# ==============================================================================================
# amigos de amigos sem vc
def amigo_de_amigo_sem_vc(usuario):
    vetorvazio = []
    for amigos in usuario["amigos"]:
        for x in lista_nomes[amigos["id"]]["amigos"]:
            if x["id"] != usuario["id"]:
                vetorvazio.append(x)

    return {"id":usuario["id"],"networking":len(vetorvazio),"amigos_de_amigos":vetorvazio}

 
  
conexoes = []
for pessoa in lista_nomes:
    conexoes.append(amigo_de_amigo_sem_vc(pessoa)) 
    #vai repetir caso eu conheça 1 e 2 e eles se conheçam vai aparecer 1,2. se ambos conhecerem algum esse alguem aparece 2 vezes
# print(conexoes)
# ==============================================================================================
# ==============================================================================================
# amigo de amigo sem repetir as pessoas 
def amigo_de_amigo_sem_vc_sem_repetir(usuario):
    vetorvazio = []
    for amigos in usuario["amigos"]:
        for dadosAmigoAmigo in lista_nomes[amigos["id"]]["amigos"]:
            if dadosAmigoAmigo["id"] != usuario["id"] and dadosAmigoAmigo not in vetorvazio:
                vetorvazio.append(dadosAmigoAmigo)

    return {"id":usuario["id"],"networking":len(vetorvazio),"amigos_de_amigos":vetorvazio}

conexoesNrepete = []
for pessoa in lista_nomes:
    conexoesNrepete.append(amigo_de_amigo_sem_vc_sem_repetir(pessoa))
    #legal! aqui não repete mais as pessoas, entretanto temos o problema que se meu amigo conhece outro amigo ambos aparecem
# print(conexoesNrepete)
# ==============================================================================================
# ==============================================================================================
# listaAmigosNaoConheco
#amigo de amigo sem repetir eu e amigos que tenho 
def listaAmigosNaoConheco(usuario):
    resultado = []
    for meusAmigos in usuario["amigos"]:
        for dadosAmigoAmigo in lista_nomes[meusAmigos["id"]]["amigos"]:
            if dadosAmigoAmigo["id"] != usuario["id"] and dadosAmigoAmigo not in resultado and dadosAmigoAmigo not in usuario["amigos"]:
                resultado.append(dadosAmigoAmigo)
    #ANC amigos que não conheço
    #ANCqtdd amigos que não conheço quantidade
    return {"id":usuario["id"],"ANCqtdd":len(resultado),"ANC":resultado}

naoConheco = []
for pessoa in lista_nomes:
    naoConheco.append(listaAmigosNaoConheco(pessoa))
# print(naoConheco)
# ==============================================================================================
# ==============================================================================================
'''
AGORA VEJAMOS UMA FORMA DE REFAZER ISSO SÓ QUE EM PYTHONIC 
''' 


# ==============================================================================================
# ==============================================================================================

# lista_interesses = [ 
#     (0,"Hadoop"),(0,"Big data") (0,"Hbase"), (0, "java"),
#     (0,"Spark"), (0,"Storm"), (0,"casandra"), (1,"postgres"),
#     (2,"python"),(2,"scipy"), (3,"statistics"), (3,"regression"),
#     (4, "machine learning"), (4,"regression"), (5,"java"), (5,"R"),
#     (6, "theory")
# ]

# ==============================================================================================
# ==============================================================================================