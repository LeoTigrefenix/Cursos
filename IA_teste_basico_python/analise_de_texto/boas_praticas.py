#=====================================================================================================================
# Algoritmo para fornecer uma breve descrição de boas práticas de refatoração de código
#
# V 2.0
#=====================================================================================================================


"""
A entrada será uma string de texto que representa um bom promtp de pesquisa para IAs Generativas.
Algoritmo fornecer uma breve descrição de boas práticas de refatoração de código em três áreas específicas: 
identificação clara de funções, separação da entrada de dados e uso de nomes descritivos para variáveis e funções.
Cada descrição deve indicar como o código pode ser melhorado nesses aspectos.
O objetivo é simularmos a ação de pesquisas em IAs Generativas de busca e pesquisa, dessa forma, cada entrada simula um bom prompt de pesquisa.
"""


# funções para suprir a função processar_entrada
def identificar_funcoes(texto):
    # Retorna uma mensagem sobre separar funções em unidades coesas e com responsabilidades únicas.
    return "Separe funções em unidades coesas e com responsabilidades únicas."

def entrada_de_dados(texto):
    # Retorne uma mensagem sobre validar e normalizar as entradas para evitar inconsistências.
    return "Valide e normalize as entradas para evitar inconsistências."

def nomenclatura_significativa(texto):
    # Retorne uma mensagem sobre usar nomes descritivos para variáveis e funções.
    return "Use nomes descritivos para variáveis e funções."
#----------------------------------------------------------------------------------------------------------------

#função que vai processar a entrada de texto
def processar_entrada(texto):
    texto = texto.lower()
    
    # Dicionário mapeando textos para funções
    opcoes = {
        "dica de boas práticas de refatoração de código, nas funções.": identificar_funcoes,
        "dica de boas práticas de refatoração de código nas funções.": identificar_funcoes,
        "dica de boas praticas de refatoraçao de codigo, nas funçoes.": identificar_funcoes,
        "dica de boas práticas de refatoração de código, nas entrada de dados.": entrada_de_dados,
        "dica de boas práticas de refatoração de código nas entrada de dados.": entrada_de_dados,
        "dica de boas práticas de refatoração de codigo, nas entrada de dados.": entrada_de_dados,
        "dica de boas práticas de refatoração de código, nomenclaturas.": nomenclatura_significativa,
        "dica de boas práticas de refatoração de código nomenclaturas.": nomenclatura_significativa,
        "dica de boas práticas de refatoração de codigo, nomenclaturas.": nomenclatura_significativa
    }

    # Verifica se o texto está presente nas opções
    if texto in opcoes:
        # Chama a função correspondente ao texto e retorna o resultado
        return opcoes[texto](texto)
   
    #vou analisar se possui o termo desejado    
    termos_respostas = {
    "nas funções"           : identificar_funcoes,
    "nas funçoes"           : identificar_funcoes,
    "nas funcões"           : identificar_funcoes,
    "nas funcoes"           : identificar_funcoes,
    "nas entrada de dados"  : entrada_de_dados,
    "nomenclaturas"         : nomenclatura_significativa
    }

    # Verifica cada termo no texto e retorna a resposta correspondente
    for termo, resposta in termos_respostas.items():
        if termo in texto:
            return termos_respostas[termo](texto)
    #caso não seja um das três opções que estamos trabalhando então retorna opção invalida:
    return "Opção inválida."

#funcao de inicialização, para pedir entrada textual ao usuário e depois, pós processamento, dar uma resposta
def inicializacao():
    # Solicita uma entrada do usuário
    entrada = input("Digite um promtp de pesquisa para IA generativa   :")
    # Processa a entrada e obtém a saída
    saida = processar_entrada(entrada)
    # Exibe a saída
    print(saida)

#chamar inicialização
inicializacao()