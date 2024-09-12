#=====================================================================================================================
# Algoritmo para analisar se um certo prompt está adequado com parametros escolhidos.
#
# V 1.4
##=====================================================================================================================


"""
Algoritmo que avalia se um prompt fornecido pelo usuário está adequado. 
O programa solicitará ao usuário que insira um prompt e, em seguida, verificará se o prompt contém palavras-chave relevantes.
As palavras-chave consideradas relevantes serão "inteligência artificial", "sistemas de recomendação online", "exemplo de conversação", "explique conceitos" e "dicas de tecnologia".
Se o prompt incluir pelo menos uma dessas palavras-chave, o programa informará que o prompt está adequado; caso contrário, ele indicará que o prompt não está adequado e sugerirá ao usuário que inclua palavras-chave relevantes.
"""



#importar biblioteca
import re


# Entrada do usuário
entrada_usuario = input("Digite algo: ")

# quebrar o texto da entrada em palavras
input_palavras = re.findall(r'\b\w+\b',entrada_usuario.lower())

# Função para avaliar se o prompt está adequado
def avaliar_prompt(prompt):
    #constantes
    count_prompts = 0;
    # Verifica se o prompt contém palavras-chave relevantes
    #palavras_chave = ["inteligência","artificial", "sistemas de recomendação online", "exemplos de" "conversação", "explique conceitos", "dicas de tecnologia" ]
    termos_chave = [
        "sistemas de recomendação onlines",
        "sistemas de recomendação online",
        "sistema de recomendação online",
        "sistemas de recomendações online",
        "sistemas de recomendacoes online",
        "sistemas de recomendações onlines",
        "sistemas de recomendaçao online"
        "sistemas de recomendação online"
        "sistemas de recomendacao online"
        "explique conceitos",
        "explique conceito",
        "expliquem conceitos",
        "expliquem conceito",
        "dicas de tecnologia",
        "dica de tecnologia"
        "exemplo de conversação",
        "exemplo de conversacão",
        "exemplo de conversacao",
        "exemplo de conversaçao",
        "exemplos de conversacão",
        "exemplos de conversacao",
        "exemplos de conversaçao",
        "exemplos de conversação",
        "inteligencia artificiais",
        "inteligencias artificiais"
        "inteligencia artificial",
        "inteligência artificial",
        ]
    
    # TODO: Aplique a condição necessária para verificar se o prompt está ou não adequado de acordo com o enunciado
    for termo in termos_chave:
        if termo in prompt.lower():
          count_prompts = count_prompts+1 
    
    #count_prompts = count_prompts + sum(palavra in palavras_chave for palavra in input_palavras)
    if(count_prompts > 0):
      return "O prompt está adequado."
    else:
      return "O prompt não está adequado. Inclua palavras-chave relevantes."
# Avaliar o prompt do usuário
feedback_usuario = avaliar_prompt(entrada_usuario)

# Exibir feedback
print(feedback_usuario)