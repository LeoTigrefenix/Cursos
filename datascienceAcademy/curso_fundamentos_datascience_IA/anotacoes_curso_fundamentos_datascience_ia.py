######################################################################################################
#
#    ANOTAÇÕES , está em python para poder por código se quiser
#
######################################################################################################

#=====================================================================================================
# Parte 1

ciencia_de_dados = {
                        "matematica_e_estatistica": "análise numérica quantitativa. Fornece as técnicas utilizadas para tratar e manipular os dados",
                        "ciencia_da_computacao":    "métodos de automatização e poder computacionál. Ferramentas de execução e redução do tempo de execução",
                        "areas_de_negocio":         "regras do jogo, objetivos, analisar os dados qualitativamente e extrair conhecimento dos dados ",
                        "dados":                    "fonte da informação"

                    }


THE_SCIENCE = "parte fundamental, pois um punhado de dados não é nada além de um punhado de bits. Precisa de métodos científicos para extrair dos dados o que ele dizem de forma direta a indireta"

if ciencia_de_dados:
    take_good_action = True


#conceito data driven
def DATA_DRIVEN(dado):
    action = ["?"]

    o_que_aconteceu         =   dado[0]
    o_que_deve_ser_feito    =   dado[1]
    acontera_novamente      =   dado[2]
    frequencia_ocorrencia   =   dado[3]
    por_que_ocorreu         =   dado[4]

    formular_decisao = o_que_aconteceu * o_que_deve_ser_feito * acontera_novamente * frequencia_ocorrencia * por_que_ocorreu 

    action.append(formular_decisao)

    return action

# ETAPAS PARA IMPLEMENTAR UM PROJETO DE CIÊNCIAS DE DADOS

def implementar_projeto(definicao_problema,coleta_armazenamento_dados):

    # preparar os dados 
    dados_prontos_formatados = limpeza_preparacao_dos_dados(coleta_armazenamento_dados)

    # processo de limpeza dos dados
    def limpeza_preparacao_dos_dados(dados_in):
        dados_arrumados = {"1": dados_in}
        return dados_arrumados
    
    # processo de análise matemática dos dados. Explorar os dados
    def analise_exploratoria(conhecimento_mais_objetivo, dados_in):
        
        with open("conhecimento.txt","w") as file:
            file.write(f"com conhecimento matemático e de computação com as definições do problema da para pegar os dados {dados_in}")
            file.write(f" não perca o foco do objetivo e dos conhecimentos de contexto {conhecimento_mais_objetivo}")

    # modelar os dados     
    modelagem_preditiva_estatistica = [analise_exploratoria(dados_prontos_formatados)]
    # avaliação e teste
    def avaliar_testar(input):
        return input*input  # faça todos os dados necessários
    
    # analise do dados obtidos
    confirmacao = avaliar_testar(modelagem_preditiva_estatistica)

    # conclusão
    if confirmacao == True:
        return 'pronto'


# defina bem seus problemas 
########################################################################################################
        
########################################################################################################
# COLETA E ARMAZENAMENTO DE DADOS 

# -> API ; Bancos de dados; fontes internas da empresa e fontes externas ; entrevistas 
data_lake = "porrada de dados bagunçados"

# coleta
def pegar_dados(input):
    API = True
    return API * input

dados_coletados = pegar_dados(data_lake)

#formatação
def formatar_dados(input):

    limpeza = True
    transformacao   = True
    integracao  = True
    combinacao  = True
    reducao = True

    


dados_formatados = formatar_dados(dados_coletados)



#============================================

# Analise exploratória de dados (EDA)
# Precisa limpar e  transformar os dados na EDA para facilitar a análise e comunicar insights 
# Nessa análise entende-se as principais características dos dados, como é a distribuição estatística e detectar ouliers (valores descrepantes)

# modelagem preditiva
## prever valores futuros ou resultados baseados em dados históricos
## otimizar precisão das previsões, sem se preocupar com a interpretabilidade do modelo (entender como ele funciona)

# modelogame estatística 
## entender relaçoes entre variáeis identificar padrões, fazer inferências sobre populações baseadas em amostra
## estabelece relações causais e assosiativas, testa hipóteses e constroi modelos explicativos 

# nem todos projetos de ciência de dados precisa de machine learning e IA, agora todo projeto de machine learning e IA precisa de ciência de dados.

