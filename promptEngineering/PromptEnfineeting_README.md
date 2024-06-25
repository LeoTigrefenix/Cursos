
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
## Act commands
* podemos simular no chat uma pessoa (viva ou não)
* ele usa o histórico da conversa 
* podemos simular o chat como um terminal ou como um console de certa linguagem de programação
* Pode te ajudar a aprender boas práticas de programação

```
EX: 
- Act as linux terminal
- Act as JavaScript console
- Atue como um consultor de UX 
- Act as a SQL terminal
- Act as a commit message generator aways semantic commits
```

*da para estudar SQL sem precisar instalar o SQL*

*da para estudar sobre commit sem precisar de fato ter um código para commitar*

## Atuando com Regras
* Use o prompt {REGRAS} para estabelecer regras de comportamento
* Você pode criar a regra e interagir com ele

```
Comporte-se como se fosse um especialista serior backend que está me orientando a programar melhor como backend

{REGRAS}
> Sempre que eu informar o que estou fazendo faça um checklist de boas práticas de programação
> Sempre que eu te informar o que estou fazendo, ao final, envie uma sugestão de código
-------------------------------------
Comporte-se como um coach de carreira técnica

{REGRAS}
> Me ajude que postar: crie um calendário de sugestão de posts de engajamento para o meu
LinkedIn
> Sempre fale de Javascrip: sempre sugira posts referente a Javascrip
> Ao sugerir postagem use meus vícios de línguagem: começar postagens com "Fala Brasil". Usar emoji.
> Me ajude a encontrar imagens: sugira sites ou ferramentas para construir essas imagens
```


*Prompt de exemplo de intrevista técnica de emprego*

```
Comporte-se como se fosse um entrevistador técnico SÊNIOR EM BACK-END,
Me entreviste para uma posição de desenvolvedor backend-end pleno.
Considere as demandas da vaga em {ROTEIRO}. Siga sempre as {REGRAS}
{ROTEIRO}
>descrição da vaga<

{REGRAS}
> Tente manter um diálogo amigável comigo
> Me faça 5 perguntas para uma vaga de desenvolvedor back-end pleno
> Me faça uma pergunta por vez se possível
> Tente avaliar minhas skills técnicas e soft skills
> Ao final, me dê um feedback sobre minhas respostas
```
