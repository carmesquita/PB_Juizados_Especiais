# Project Charter - TP3 Juizados Especiais

**Autora:** Carolina Gabriela Mesquita

## Problema

Os dados do CNJ permitem comparar o tempo médio até a sentença nos Juizados Especiais, mas essa comparação não é apresentada de forma simples para todos os Tribunais de Justiça.

**Pergunta do projeto:** como o tempo médio até a sentença varia entre os 27 Tribunais de Justiça?

## Escopo

O projeto apresenta dados de 2025 dos 27 Tribunais de Justiça estaduais, notícias sobre Juizados Especiais e um espaço para envio de informações complementares.

No TP3, a aplicação será organizada em múltiplas páginas e contará com uma API em FastAPI, com rotas GET e POST documentadas.

Os textos das notícias serão mantidos em formato estruturado para futuro uso com LLMs. O Selenium será adotado somente se uma nova fonte exigir interação dinâmica.

Não fazem parte do projeto a análise de processos individuais, a previsão de prazos ou a avaliação de magistrados e unidades judiciais.


## Objetivos

- comparar o tempo médio até a sentença entre os tribunais;
- permitir filtrar, ordenar e consultar os dados;
- permitir upload e download de CSV;
- apresentar notícias coletadas do portal do CNJ;
- organizar a aplicação em múltiplas páginas;
- disponibilizar dados por meio de uma API com rotas GET e POST;
- preparar os textos das notícias para futuro uso com LLMs.


## Público e ODS

O público é formado pelo professor, alunos e pessoas interessadas em dados públicos da Justiça. O tema está relacionado à ODS 16, sobre acesso à Justiça e instituições eficazes.

## Critérios de sucesso

- apresentar os 27 tribunais;
- mostrar média, menor e maior tempo;
- disponibilizar gráfico, tabela, filtros, upload e download;
- manter a comparação escolhida durante a sessão;
- exibir as notícias coletadas com Beautiful Soup;
- disponibilizar menu de navegação entre as páginas;
- disponibilizar e documentar as rotas da API;
- manter títulos e resumos das notícias em formato estruturado.

## Riscos

- o portal do CNJ pode ficar indisponível;
- a estrutura da página de notícias pode mudar;
- o indicador agregado pode ser confundido com a duração de processos individuais.

Os CSVs processados ficam salvos no projeto e a limitação do indicador é informada no painel.
