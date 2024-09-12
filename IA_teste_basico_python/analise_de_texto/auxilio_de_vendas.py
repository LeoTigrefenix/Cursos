#=====================================================================================================================
# Algoritmo para  ajudar a listar produtos mais baratos que o solicitado, dentro da sequencia estabelecida na lista 'catalogo'
#
# V 2.3
#=====================================================================================================================


"""
Programa que simule o auxílio de vendas de um site de catálogos de cogumelos utilizando inteligência artificial (sqn)
O intuito é oferecer aos clientes sugestões de cogumelos que estão em promoção.
Permite-se que o usuário informe o nome de um cogumelo desejado e, com base nessa informação, se sugere até dois cogumelos adicionais da lista, cujos valores sejam iguais ou menores que o do cogumelo selecionado pelo cliente.
No caso de não houver sugestões disponíveis, ou seja, se o cogumelo escolhido for o mais caro, se exibe uma mensagem indicando que não há sugestões
"""

# Entrada do usuário
cogumelo_desejado = input()

# Função para sugerir cogumelos com preços mais baixos com base em um cogumelo desejado.
def sugerir_cogumelos(cogumelo_desejado):
    #deixar minusculo
    cogumelo_desejado = cogumelo_desejado.lower()

    #Defina um dicionário onde as chaves são os tipos de cogumelos e os valores são os preços correspondentes
    catalogo = {
        "shitake"   : 10,
        "portobello": 8,
        "shimeji"   : 6,
        "champignon": 12,
        "funghi"    : 16,
        "porcini"   : 16
    }


   # Verifica se o cogumelo desejado estão no catálogo
    if cogumelo_desejado in catalogo:
        # Se estiver no catálogo, armazene o preço do cogumelo desejado e crie uma lista vazia para as sugestões
        valor_desejado = catalogo[cogumelo_desejado]
        sugestoes = []
        
        # Procura por cogumelos mais baratos no catálogo. Vai rodar a 1ª coluna do catalogo olhando para o valor na 2ª coluna
        for cogumelo, valor in catalogo.items():
            if valor <= valor_desejado and cogumelo != cogumelo_desejado:
                sugestoes.append((cogumelo, valor))  # Adiciona uma dupla (cogumelo, valor)
                if len(sugestoes) == 2:
                    #para o loop do for
                    break
        
        if not sugestoes:
            # Se não houver sugestões, exiba a mensagem indicada no enunciado
            print("Desculpe, não há sugestões disponíveis.")
        else:
            #Vai rodar a 1ª coluna do valor_sugestao olhando para o valor na 2ª coluna
            for sugestao, valor_sugestao in sugestoes:
                #ajuste para colocar a primeira letra maiúscula. O 1: é para pegar todas as demais letras.
                print(f"{sugestao[0].upper() + sugestao[1:]} - Valor: {valor_sugestao}")
    else:
        # TODO: Se o cogumelo desejado não estiver no catálogo, exiba uma mensagem de erro indicada no enunciado
        print("Cogumelo não encontrado no catálogo.")

# Chamada da função para sugerir cogumelos
sugerir_cogumelos(cogumelo_desejado)