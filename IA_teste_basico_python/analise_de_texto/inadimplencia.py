#=====================================================================================================================
# Algoritmo para avaliar modelos de IA de detecção de inadimplência bancária
#
# V 1.2
#=====================================================================================================================


"""
Avaliar desempenho de modelos de IA usando algumas métricas de avaliação.
Recebemos n matrizes de confusão e retornamos o índice, precisão e acurácia da matriz que apresenta o melhor desempenho com base no cálculo dessas métricas.

• Acurácia é calculada pela fórmula: (VP + VN) / (VP + FP + FN + VN)
• Precisão é calculada pela fórmula: VP / (VP + FP)

Onde:

• VP (Verdadeiro Positivo): Casos em que o modelo previu corretamente a classe positiva.
• FP (Falso Positivo ou Erro Tipo I): Casos em que o modelo previu incorretamente a classe positiva.
• FN (Falso Negativo ou Erro Tipo II): Casos em que o modelo previu incorretamente a classe negativa.
• VN (Verdadeiro Negativo): Casos em que o modelo previu corretamente a classe negativa.
"""
#receber a entrada da quantidade de matrizes e transformar em inteiro
n = int(input())

"""
A entrada consiste em uma string composta por: 
n, representando o número de matrizes de confusão, seguido dos valores que compõem as n matrizes.

Cada matriz consiste em quatro valores, 
onde os dois primeiros representam a primeira linha da matriz, composta por verdadeiros positivos (VP) e falsos positivos (FP);
os dois últimos valores representam a segunda linha, que é composta por falsos negativos (FN) e verdadeiros negativos (VN). As duas linhas e os valores que as compõem estão separados por vírgulas.
"""

matrices = []

for n in range(0, n):
    #recebe as matrizes
    matrix = input()

    #Montar um vetor com as matrizes 
    #Exemplo de 3 matrizes [['50', '10', '5', '85'], ['20', '5', '8', '67'], ['30', '12', '4', '88']]
    # VP, FP, FN, VN
    matrices.append(matrix.split(','))

print(matrices)

#  Calcular o que queremos


def performance(matrices_in):
    index_salvo     = 0    
    acuracia_salva  = 0
    precisao_salva  = 0

    #para economizar memória, vamos calcular a acuracia e a precisao da matriz e comparar com o valor salvo, se for maior substitui


    #  Define Loop through each matrix to calculate metrics
    for index, matrix in enumerate(matrices_in):
        #  Define tp, fp fn and tn
        VP  = int(matrix[0])
        FP  = int(matrix[1])
        FN  = int(matrix[2])
        VN  = int(matrix[3])
        #  calcular acuracia e precisão
        acuracia_atual = (VP + VN) / (VP + FP + FN + VN)
        acuracia_atual = round(acuracia_atual,2)

        precisao_atual = VP / (VP + FP)
        precisao_atual = round(precisao_atual,2)
        #  pega o melhor caso
        if acuracia_atual > acuracia_salva and precisao_atual > precisao_salva:
            index_salvo = index+1
            acuracia_salva = acuracia_atual
            precisao_salva = precisao_atual
       
    return [index_salvo,acuracia_salva,precisao_salva]
     

resultado = performance(matrices)

print(f"Índice: {resultado[0]}")
print(f"Acurácia: {resultado[1]}")
print(f"Precisão: {resultado[2]}")

 
