#=====================================================================================================================
# Algoritmo para analisar o sentimento de um comentário fornecido pelo usuário
#
# V 1.2
##=====================================================================================================================


"""
Depois de calcular as contagens de palavras positivas e negativas, o programa determinará o sentimento predominante do comentário. 
Se houver mais palavras positivas do que negativas, o sentimento será considerado positivo. 
Se houver mais palavras negativas do que positivas, o sentimento será considerado negativo. 
Caso contrário, se houver um número igual de palavras positivas e negativas, o sentimento será neutro.
"""

# Importa o módulo re, que é a biblioteca de expressões regulares do Python. 
import re

#requisitar texto para análise
entrada_usuario = input("Digite algo: ")

def analyze_sentiment(comentario):

    # Divisão do comentário em palavras
    input_palavras = re.findall(r'\b\w+\b', comentario.lower())
    
    # Lista de palavras positivas, negativas e neutras
    positivas = [
        "bom", "boa", "ótimo", "excelente", "maravilhoso", "gostei", "incrível", "fantástico", "positivo", 
        "adorável", "excelente", "maravilhosa", "agradável", "satisfeito", "satisfatório", "surpreendente", 
        "espetacular", "lindo", "delicioso", "animado", "encantador", "positivo", "ótimos", "extraordinário",
        "melhorar em nada"
    ]
    
    negativas = [
        "ruim", "péssimo", "horrível", "terrível", "odeio", "desagradável", "chato", "frustrante", "pior", 
        "insuportável", "horrível", "desastroso", "lamentável", "abominável", "horrendo", "incômodo", 
        "desapontado", "desapontadora", "ruins", "medíocre", "negativo", "melhorar muito"
    ]
    
    neutras = [
        "mas", "deixou", "apesar", "embora", "entretanto", "contudo", "porém", "mais ou menos",
        "então", "como", "quando", "onde", "qual", "quem", "se","ainda"
    ]

    # Contagem de palavras positivas, negativas e neutras
    count_positivo = sum(palavra in positivas for palavra in input_palavras)
    count_negativo = sum(palavra in negativas for palavra in input_palavras)
    count_neutro = sum(palavra in neutras for palavra in input_palavras)
    # TODO: Conte quantas palavras neutras estão presentes no comentário.  

    # Verifica se há mais palavras positivas do que negativas no comentário e se não há palavras neutras. Se essa condição for verdadeira, o comentário é considerado positivo.
    if count_positivo > count_negativo and count_neutro == 0:
        return "Positivo"
    elif count_positivo < count_negativo and count_neutro == 0:
        return "Negativo"
    else:
        return "Neutro"
    # TODO: Complete a codição para determinar o sentimento com base na contagem de palavras

# Saída esperada
sentimento = analyze_sentiment(entrada_usuario)
print("Sentimento:", sentimento)