# Data Summary Report - TP3 Juizados Especiais

**Autora:** Carolina Gabriela Mesquita

| Fonte | Tipo de dado | Objetivo de uso | Resumo e problemas encontrados |
|---|---|---|---|
| Justiça em Números/CNJ | Estruturado - CSV | comparar o tempo médio até a sentença | 27 tribunais, ano de 2025, sem valores ausentes no arquivo processado. O dado é uma média por tribunal e não representa processos individuais |
| Notícias dos Juizados Especiais/CNJ | Não estruturado - HTML | apresentar informações de contexto e preparar uma base textual | dez notícias coletadas por requisições HTTP e Beautiful Soup. O Selenium não é necessário para a fonte atual. A estrutura da página pode mudar e exigir ajustes |
| CSV enviado pelo usuário | Estruturado - CSV | acrescentar observações sem alterar a base oficial | deve possuir as colunas `tribunal`, `observacao` e `fonte` |
| Dados complementares enviados pela API | Estruturado - JSON | receber novas observações sem alterar a base oficial | envio por rota POST com os campos `tribunal`, `observacao` e `fonte` |

## Campos utilizados

O arquivo `tempo_sentenca_juizados.csv` contém ano, tribunal, nome do tribunal, UF, tempo médio da sentença e quantidade de sentenças de conhecimento.

O arquivo `noticias_juizados.csv` contém título, data, resumo, URL e fonte da notícia.

O arquivo `noticias_para_llm.csv` contém identificador, título, resumo, texto preparado, data, URL e fonte. O campo texto reúne o título e o resumo para permitir uso futuro em tarefas com LLMs.

Os dados estatísticos e as notícias são coletados em notebooks separados e salvos em `data/processed` para uso no aplicativo.

## Decisão sobre a coleta

Não foi adicionada uma nova fonte dinâmica nesta etapa. As fontes atuais podem ser acessadas por arquivos estruturados, requisições HTTP e Beautiful Soup. O Selenium será utilizado somente se uma futura fonte exigir interação com elementos dinâmicos da página.