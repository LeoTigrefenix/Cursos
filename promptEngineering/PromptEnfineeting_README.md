
# Padrões de prompt 
## FTAE
* Me *função* um *tipo de texto* sobre *assunto* neste *estilo*

| EX: Me escreva um roteiro de vídeo sobre como pedir aumento no estilo de vídeo do Primo Rico.

    Função: escreva/resuma/traduza/crie tópico

    Tpo de text: roteiro, post para blog, poema, postagem para instagram, bullet points, cronograma de estudo

    E: estilo do filósofo tal, em história para criança, em artigo acadêmico, em carrossel do instagram , estilo informal e descontraído, influencer de tecnologia

## MELHORIAS FOCANDO EM QUEM OUVE
* crie como se fosse para *tipo de pessoa*

OU
* *função* com um tom de voz para * tipo de pessoa*

## R3 & campo semântico

* é possível criar variáveis dentro do chatgpt (login gratuito mesmo).
* utilize {} para nomear um conjunto. Embaixo dele ficará o conjunto de dados.
* utilize [] para nomear uma variável sozinha colocando o valor dela após fechar o colchetes e colocar dois pontos

```
EX:
Me escreva um artigo sobe os primeiros passos no Docker, em tom de conversa com uma criança de 10 anos. Agora use os itens em {RESUMO} para o {ROTEIRO} seguindo as {REGRAS}.

{RESUMO}
[Autoridade]:Felipe, desenvolvedor backend
[Avatar]: Desenvolvedores Júniors
[Problema]: Como instalar o Docker

{ROTEIRO}
Olá eu sou [Autoridade] e vou ajudar o [Avatar]. Vamos resolver o [Problema]

{REGRAS}
> Siga o {ROTEIRO} acima e substitua os elementos entre [] do {ROTEIRO} por aqueles listados em {REUMO} acima
```

## Uso de ""
Uma forma dele saber que é um termo literal que deve ser entendido.

    EX: "Pai rico e pai pobre"

## Planejamento
* É possível vc solicitar um planejamento falando quanto tempo por dia e quantos dias. 
* Pode separar em módulos e tópicos 
* Pode solicitar os dias da semana
* O ChatGPT vai julgar os detalhes de cada semana/dia  

## Tópicos quebrados
* Pode-ser solicitar por meio de tópicos quebrados
* E pode ainda acrescentar o R3 após ele

```
Função:
Tipo de Texto:
Assunto:
Estilo:
Tom de voz:
```
