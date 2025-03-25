######################################################################################################
#
#    ANOTAÇÕES , está em python para poder por código se quiser
#
######################################################################################################
# Dicas 
"""
Enquanto você não executar um algoritmo de aprendizado de máquina em um datasetcom milhões de registros, 
 não criar um algoritmo de limpeza e transformação de dados, não coletarstreaming  de  dados  de  redes  sociais, 
 você  não  vai  compreender  como  as  coisas  funcionam.Experimente! Aprenda, faça, erre, faça novamente 
 e quando você menos esperar, 
 você vai ser capazde analisar dados e contribuir para a empresa onde trabalha ou para seu próprio negócio
"""
"""
É preciso praticar, testar,experimentar, cometer erros, aprender com eles, testar novamente
 e ter umamentalidade orientada ao aprendizado constante
"""
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


#==========================================================================

# existem várias abordagens

## Modelagem estatística 
#### usa técnicas como regressão linear , ANOVA, Teste de hipótese 
#### pode fazer suposições assumido que os dados sigam certas distribuições e que há relações lineares entre variáveis
#### Propósito: 
"""
Entender relações entre variáveis, identificar padrões e fazer
inferências sobre populações baseadas em amostras.
Foco: Estabelecer relações causais ou associativas, testar hipóteses e
construir modelos explicativos.
"""
#### Utiliza:
"""
Ferramenta: Linguagem R, Stat, Python (Statsmodels), SAS, SPSS
Técnica: Regressão Linear, Regressão Logística, ANOVA, Análise de sobrevivênvia, Análise Fatorial, Método Probabilístico
"""

## Modelagem preditiva 
#### Aprendizado de máquina supervisionado (árvore de decisão, rede neurais, svm) e aprendizado não supervisionado (clusterização)
#### Propósito: 
"""
 Prever valores futuros ou resultados baseados em dados
históricos.
Foco: Otimizar a precisão das previsões, muitas vezes sem se preocupar
com a interpretabilidade do modelo.
"""
#### Utiliza:
"""
Ferramenta:Python(Scikit-learn, Pytorch, TensorFlow), Linguagem R, C++, Java, JS, Rust, Julia
Técnica: RandomForest, Árvore de decisão, Redes Neuras, deep learning, SVM, Boosting, Regressão Linear, Regressão Logística
"""


# ==============================================================================================
# Avaliação e Teste

## Métrica de Avaliação  
"Métricas de avaliação são indicadores utilizados para medir o desempenho de um modelo de machine learning. Exemplos comuns incluem acurácia, precisão, recall, F1-score e RMSE. A escolha da métrica depende do tipo de problema (classificação, regressão, etc.) e dos objetivos do projeto. Elas permitem quantificar quão bem o modelo está performando em relação aos dados de teste ou validação."

## Validação Cruzada  
"Validação cruzada é uma técnica para avaliar a generalização de um modelo, dividindo o dataset em múltiplos subconjuntos (folds). O modelo é treinado em alguns folds e testado no restante, repetindo o processo para cada fold. A versão mais comum é a k-fold cross-validation, onde o dataset é dividido em k partes. Isso ajuda a reduzir o viés de avaliação e fornece uma estimativa mais confiável do desempenho do modelo."

## Curva de Aprendizado  
"A curva de aprendizado é um gráfico que mostra a relação entre o desempenho do modelo (ex.: erro ou acurácia) e o tamanho do conjunto de treinamento ou o número de épocas de treinamento. Ela ajuda a identificar se o modelo está sofrendo de overfitting (desempenho bom no treino, mas ruim na validação) ou underfitting (desempenho ruim em ambos). Pode ser usada para ajustar hiperparâmetros ou decidir se mais dados são necessários."

## Análise de Erros  
"A análise de erros consiste em investigar os casos em que o modelo cometeu erros durante a previsão. Isso envolve identificar padrões nos dados onde o modelo falha, como classes específicas ou regiões do espaço de features. A análise ajuda a entender as limitações do modelo e a propor melhorias, como ajustes no pré-processamento, seleção de features ou escolha de algoritmos."

## Benchmarking  
"Benchmarking é o processo de comparar o desempenho de diferentes modelos ou algoritmos em um mesmo conjunto de dados. O objetivo é identificar qual abordagem ou técnica oferece os melhores resultados para o problema em questão. Isso pode incluir a comparação de métricas de avaliação, tempo de treinamento e complexidade do modelo, ajudando a escolher a solução mais adequada para o contexto."

# ==============================================================================================
# Entrega de projeto

## Relatório Técnico ou Científico
## Relatório Executivo
## Dashboard ou infográfico
## Aplicação WEB
## API
## Jupyter Notebook (ele gera relatório no final se manjar dos paranaue)

# ====================================================================================================

# Conseitos armazenamento de dados 

## Data Lake  
"Um Data Lake é um repositório centralizado que armazena grandes volumes de dados brutos em seu formato original, estruturados, semiestruturados ou não estruturados. Ele é projetado para armazenar dados em escala e permite que empresas armazenem dados sem precisar definir sua estrutura antecipadamente. É ideal para análises exploratórias, machine learning e processamento de big data, utilizando ferramentas como Hadoop, Spark ou AWS S3."

## Data Warehouse  
"Um Data Warehouse é um sistema de armazenamento otimizado para análise e relatórios, onde os dados são estruturados, organizados e processados para facilitar consultas e análises. Diferente de um Data Lake, os dados em um Data Warehouse são limpos, transformados e armazenados em esquemas bem definidos (como estrela ou floco de neve). É amplamente utilizado para Business Intelligence (BI) e ferramentas como SQL, Amazon Redshift ou Google BigQuery."

## Data Lakehouse  
"O Data Lakehouse é uma arquitetura moderna que combina as melhores características de um Data Lake e um Data Warehouse. Ele permite armazenar dados brutos em grande escala (como um Data Lake) enquanto oferece ferramentas de gestão e processamento estruturado (como um Data Warehouse). Essa abordagem suporta análises avançadas, machine learning e BI, com tecnologias como Delta Lake e Apache Spark, proporcionando flexibilidade e desempenho."

## Data Bricks  
"Databricks é uma plataforma unificada de análise de dados e machine learning, baseada no Apache Spark. Ela permite processar grandes volumes de dados em tempo real, realizar análises avançadas e construir modelos de machine learning. A plataforma é conhecida por sua integração com Data Lakes e Data Warehouses, oferecendo ferramentas para ETL, visualização de dados e colaboração entre equipes. É amplamente utilizada em ambientes de nuvem, como AWS, Azure e Google Cloud."

## ETL
"extract transform load -> extrair dados, aplicar transformação e armazenar"
## ELT
"extract load transform -> extrair dados, armazenar e no armazenamento da para fazer a transformação"
#=========================================================================================================

# Machine Learning 
###As quatro abordagens básicas utilizadassão aprendizado supervisionado, aprendizado não supervisionado, aprendizado por reforçoe aprendizado profundo
"""
Existem  diversos  algoritmos  de  aprendizagem  de  máquina,
dependendo  se  aaprendizagem é supervisionada ou não supervisionada,
tais como: Linear Regression,
Ordinary  Least  Squares  Regression  (OLSR),
Logistic  Regression,
Classification  andRegression  Tree  (CART),
Naive  Bayes,
Gaussian  Naive  Bayes,
k-Nearest  Neighbour(kNN),
k-Means,
Bootstrapped Aggregation (Bagging),
Natural Language Processing(NLP),
Principal Component Analysis (PCA),
Principal Component Regression (PCR),
BackPropagation e muito mais.
"""

"""
Machine Learning (ML) é uma forma de Inteligência Artificial (IA) que permite que um sistemaaprenda com dados ao invés de programação explícita.
Depois que um algoritmo de ML é escrito, ele deve ser “treinado” antes de ser implantado em seuuso  pretendido.  
O  treinamento  é  o  processo  pelo  qual  a  máquina  aprende.  Algoritmos  sãoalimentados com dados de treinamento, possibilitando a produção de modelos. O modelo aprendeo padrão nos dados (se o padrão existir) e, ao receber novos dados, é capaz de detectar o padrão efazer previsões.Por  meio  de  seu  treinamento  e  aprendizado  online  iterativo,  um  modelo  deaprendizado de  máquina  pode  melhorar  muito  sua  compreensão  dos  tipos  deassociações que existem entre os elementos de dados. Devido à sua complexidade etamanho,  esses  padrões  e  associações  seriam  facilmente  ignorados  pela  observaçãohumana.  Técnicas  de  aprendizado  de  máquina  são  necessárias  para  melhorar  aprecisão  das  análises.  Dependendo  da  natureza  do  problema  de  negócio,  existemdiferentes abordagens com base no tipo e no volume dos dados.

"""

"""
O aprendizado supervisionado é usado com dados já fornecidos com rótulos, por exemplo, identificaçãode animais a partir de novas imagens.
O  aprendizado  não  supervisionado  é  usado  com  dados  não  rotulados  e  geralmente  é  usado  paraidentificar e-mails de spam ou segmentar clientes por similaridade.
O aprendizado por reforço é semelhante ao aprendizado supervisionado, pois usa dados rotulados. Noentanto, o aprendizado por reforço é feito sem o benefício dos dados de treinamento, melhorando suamodelagem por tentativa e erro de dados do mundo real.
O  aprendizado  profundo (Deep  Learning)  incorpora  redes  neurais  para  aprender  com  os  dados  demaneira  iterativa.  É  especialmente  útil  no  aprendizado  de  padrões  de  dados  não  estruturados  emaplicativos  de  Processamento  de  Linguagem  Natural  e  Visão  Computacional.  Há  modelos  de  DeepLearning para aprendizado supervisionado, não supervisionado e por reforço
"""

# =======================================================================================================
# Apresentação de dados  com um bom story telling 
"""
Tableau,
Metabase,
Microsoft Excel,
Microsoft Power BI,
Microstrategy,
Weka,
NetworkX,
Gephi,
bibliotecas  Java  Script  (D3.js,
Chart.js,  Dygraphs),além de visualizações de alto nível que podem ser feitas em Python ou R
"""

#=======================================================================================
# LINKS

"""
Blogs
Data Science Central: https://www.datasciencecentral.comKDD 
Nuggets: http://www.kdnuggets.comArtigos 
sobre R: http://www.r-bloggers.comPython 
Brasil: http://python.org.br
Ciência e Dados:
 http://www.cienciaedados.comEstatísticaStatistics: 
http://www.statistics.comSimply 
Statistics: http://simplystatistics.org
Machine Learning e IAHugging Face: https://huggingface.co
Deep Learning Book Brasil: https://www.deeplearningbook.com.brVídeos,
 Competições e Tutoriais
Data Science for Social Goods: 
http://dssg.uchicago.edu
Kaggle: https://www.kaggle.com
Towards 
Data Science: https://towardsdatascience.comCap

"""
#=======================================================================================
# Eng de Dados
"""
Faça Uma Auto-AnálisePasso 
Domine Pelo Menos UmaLinguagem de ProgramaçãoPasso 
Desenvolva Suas HabilidadesSobre Governança e Segurança de DadosPasso 
Domine o Sistema Operacional LinuxPasso  
Desenvolva  Suas  Habilidades  emCloud Computing e Computação DistribuídaPasso 
Aprenda a Projetar, Implementar eManter Data LakesPasso 
Aprenda a Trabalhar com Bancos deDados Relacionais e Linguagem SQL
"""

#=======================================================================================
# Eng de IA
"""
Um Engenheiro de IA normalmente precisa executar determinadas tarefas comodesenvolver,
 testar e implantar modelos de IA por meio de algoritmos de aprendizado demáquina. 
 As responsabilidades incluem:
 Converter  os  modelos  de  aprendizado  de  máquina  em  interfaces  de  programa  deaplicativo  (APIs)  para  que  outros  aplicativos  possam  usá-los.  Embora  um Engenheirode  Machine  Learning  possa  ser  responsável  por  essa  tarefa,
 a  empresa  pode  não  terprofissionais  com  esse  perfil  e  cabe  ao  Engenheiro  de  IA  saber  gerar  a  API,  porexemplo.
 Criar modelos de IA do zero e ajudar diferentes áreas e interessados dentro de umaempresa  (como  gerentes  de  produto  e  áreas  de  negócio)  a  entender  quaisresultados eles obtêm do model
 Criar uma infraestrutura de ingestão e transformação de dados para o treinamento demodelos  ou  mesmo  após  o  deploy.  Embora  um Engenheiro  de  Dados  possa  serresponsável  por  essa  tarefa,  a  empresa  pode  não  ter  profissionais  com  esse  perfil  ecabe ao Engenheiro de IA garantir que os dados cheguem até os modelos
 Criar modelos de IA diversos .
 Desenvolva suas habilidades em arquiteturas CNN, GAN e Transformers, pelomenos para começar. Então, poderá avançar para arquiteturas mais complexas,normalmente encontradas em LLMs
"""

"""
Hoje PyTorch e TensorFlow são os mais usados em IA e recomendamos o PyTorch,principalmente para os iniciantes.Aprendendo bem um framework será mais fácil aprender um segundo, se necessário,para algum projeto
"""
##  dominar pelo menos um framework
"""
Hoje PyTorch e TensorFlow são os mais usados em IA e recomendamos o PyTorch,principalmente para os iniciantes.Aprendendo bem um framework será mais fácil aprender um segundo, se necessário,para algum projeto.Além disso, é importante dominar o conceito de Transfer Learning (Transferência deAprendizado) quando usamos modelos pré-treinados e ajustamos esses modelos comnossos próprios dados, o que reduz custo e tempo de desenvolvimento da solução
"""

## Arquitetura e eng de software 
""" 
Compreenda os Fundamentos de Engenharia de Software Engenheiro de Machine Learning tem como função principal construir soluçõesde  software  baseadas  em  Machine  Learning.  
Mas  construir  um  software  não  éalgo  trivial  e  requer  conhecimentos  que  vão  desde  arquitetura  até  padrões  dedesenvolvimento. Esse conhecimento será importante para saber a melhor formade  acoplar  um  modelo  de  Machine  Learning  em  uma  aplicação  que  realizarádiversas outras tarefas como controle de sessão, autenticação, consulta a bancode dados, envio de e-mails, etc... 
Machine Learning é apenas um “pedaço” de umsoftware  maior  e  compreender  como  incluir  esse  “pedaço”  em  um  softwarerequer conhecimentos em engenharia de software.Aliás, essa é uma habilidade crítica nos dias de hoje, uma vez que o mundo já égovernado por software.Data Science Academy leonardo.tancredi@optdriven.com.br 67b3468bcef6d4f4aa07201a
"""
## Proficiente em MLOps

"""
Ao integrar práticas de CI/CD(Continuous Integration/ContinuousDeployment) e automação depipelines de dados, MLOps facilita agestão de modelos em larga escala,promovendo eficiência e consistêncianos projetos de Machine Learning.
A adoção de MLOps envolve aimplementação de pipelinesautomatizados que garantem arepetibilidade e a confiabilidade dosprocessos de ML, facilitando aatualização contínua dos modeloscom novos dados e ajustes conformenecessário.
Com a crescente complexidade eescala dos projetos de ML, MLOps setorna essencial para manter aeficiência operacional, reduzir custose riscos, e assegurar que as soluçõesde ML possam entregar valorcontínuo ao negócio.
MLOps possibilita uma abordagemmais robusta e sistemática para agestão do ciclo de vida dos modelos,promovendo uma cultura de inovaçãocontínua e melhoria dentro dasorganizações
"""
#=======================================================================================
#Arquiteto de Dados
## o Arquiteto de dados projeta
## o Engenheiro de dados executa
"""
Que é Arquitetura de Dados?
Arquitetura  de  Dados  é  a  estrutura  organizacionalalinhada    aos    processos    de    negócios    quepadronizam o processo de coleta, armazenamento,transformação, distribuição e uso de dados.A   estrutura   é   criada   para   proteger   dadosconfidenciais,  tornando  as  partes  mais  relevantesacessíveis  por  pessoas  autorizadas  no  momentocerto
Em outras palavras, podemos definir Arquitetura de Dados como:“Um conjunto de regras, políticas e modelos que determinam que tipo dedados são coletados e como são usados, processados e armazenados”

O Arquiteto de Dados também define os processos envolvidos no teste e manutenção debancos de dados e sistemas de armazenamento.O Engenheiro deDados ExecutaO Arquiteto deDados ProjetaData 
Neste  debate  entre  Arquiteto  de  Dados  e  Engenheiro  de  Dados,  enquanto  oprimeiro projeta e planeja a estrutura de dados, o segundo coloca esse projeto emação para construir a infraestrutura de dados de uma empresa.
"""

""" 
Desenvolver e implementar uma estratégia geral de dados que esteja alinhada com osprocessos de negócios. A estratégia inclui projetos de modelos de dados, padrões dedesenvolvimento  de  banco  de  dados,  implementação  e  gerenciamento  de  DataWarehouses e Data Lakes e sistemas de análise de dados, além de pipelines de dados
Gerenciar a arquitetura de dados end-to-end, desde a seleção da plataforma, desenhoda  arquitetura  técnica  e  implementação,  até  finalmente  testar  e  implementar  asolução proposta
"""

"""
Conduzir  auditoria  contínua  do  desempenho  do  sistema  de  gerenciamento  dedados, refinar sempre que necessário e relatar imediatamente qualquer violaçãoou brecha às partes interessadas
"""

"""
Esteja Familiarizado com Orquestração de Fluxos de Dados eModern Data Stack
"""

## governança de dados
"""
Esse tipo de sistema sinaliza e reconcilia problemas e organiza dados corrompidos,defeituosos, desatualizados ou redundantes, de acordo com as regras de retenção. 
Essa é uma das tarefas de um Arquiteto de Dados. Você precisa desenvolver suas habilidades emGovernança de Dados conhecendo os processos e ferramentas
Precisa ficar atento a condição dos dados combase em fatores como precisão,integridade, consistência,confiabilidade e se estão atualizados.
"""
### -> O Apache Airflow é atualmente a principal ferramenta para orquestração defluxos de dados e faz parte do Modern Data Stack.Data Science Academy leonardo.tancredi@optdriven.com.br 67b3468bcef6d4f4aa07201a
### -> Ahh, e não esqueça deLinguagem SQL. Isso é omínimo de conhecimentoque se espera de umArquiteto de Dados.Data Science Academy leonardo.tancredi@optdriven.com.br 67b3468bcef6d4f4aa07201a

### Pepiline de dados 
"""
 pipeline de dados é como se fosse uma linha de produção, por onde os dados vãop assando   desde   a   origem   e   então   vão   recebendo   limpeza,
 transformação,enriquecimento,   documentação,   gestão   de   metadados,   governança,   tags   deidentificação,  até  chegarem  no  seu  destino  
 e  serem  usados  para  análise,  arquivadosou descartados
"""

#=======================================================================================
# DataOps
### é uma metodologia automatizada 
"""
ssa abordagem enfatiza aautomação  de  processos  de  dados,  a  integração  contínua  e  a  entregacontínua (CI/CD) de dados e insights, 
buscando reduzir os tempos de ciclo,aumentar a eficiência e garantir a qualidade e a confiabilidade dos dados
"""

## Passos
### Definição  de  Processos:  
"Defina  os  processos  e  fluxos  de  trabalho  para  os  pipelines  de  dados,incluindo a integração, validação, teste e implantação"
### Automatização
"Automatize tarefas repetitivas para melhorar a eficiência e a precisão. Isso incluia automação de testes, implantações e atualizações"
### Colaboração entre o time de dados 
"Crie uma equipe cross-funcional de desenvolvimento de software e de dados paratrabalhar juntos na criação, manutenção e monitoramento dos pipelines de dados"
### Monitoramento
"Monitore o desempenho de cada pipeline de dados para identificar problemase oportunidades de melhoria"
### Feedback
"Implemente um sistema de feedback para permitir que as equipes de desenvolvimentode software e de dados possam compartilhar informações e soluções em tempo real"
### Cultura de melhoria
"Fomente  uma  cultura  de  experimentação,  inovação  e  melhoria  contínua  para  garantirque  todos  estejam  sempre  procurando  formas  de  tornar  cada  pipeline  de  dados  mais  eficiente  eeficaz"
### DataOps mexe com o ciclo de vida dos dados , MLOps mexe com o ciclo de vida dos modelos
"""
DataOps  é  uma  abordagem  de  gerenciamento  de  dados  que  tem  como  objetivo  aumentar  avelocidade,  qualidade  e  eficiência  do  ciclo  de  vida  dos  dados.  DataOps  se  concentra  emautomatizar  e  otimizar  processos  de  coleta,  armazenamento,  processamento  e  distribuição  dedados.Já  MLOps  é  uma  extensão  do  DataOps  que  se  concentra  especificamente  no  gerenciamento  dociclo  de  vida  dos  modelos  de  aprendizado  de  máquina  (Machine  Learning).  Isso  inclui  tarefascomo  o  treinamento,  o  teste  e  o  monitoramento  de  modelos,  bem  como  a  implementação  e  ogerenciamento de modelos em produção.
Enquanto DataOps pode ser responsabilidade de um Engenheiro de Dados ou de um EngenheiroDataOps, MLOps é responsabilidade do Engenheiro de Machine Learning.
"""

## Ferramentas dataops
"""
Apache Spark faz ipelines de ETL
Apache  Airflow:  um  sistema  de  orquestração  de  pipelines  de  dados  baseadoem tarefas.
AWS Glue: um serviço de ETL da Amazon Web Services que permite a criação,execução e gerenciamento de pipelines de dados.
Talend:  uma  plataforma  de  integração  de  dados  que  oferece  ferramentaspara coletar, integrar e distribuir dados.
Airbyte: ferramenta open-source para movimentação de dados entre sistemasheterogêneos.
StreamSets:  uma  plataforma  de  gerenciamento  de  dados  que  permite  acriação, execução e monitoramento de pipelines de dados.
DataKitchen: uma plataforma de automação em DataOps.Ferramentas de DataOps
Ferramentas de CI/CD: Jenkins, GitLab CI
"""

#=======================================================================================
# Analytics Engineer