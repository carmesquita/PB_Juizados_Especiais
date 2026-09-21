# Data Summary Report - TP2 Juizados Especiais

**Autora:** Carolina Gabriela Mesquita

| Fonte | Tipo de dado | Objetivo de uso | Resumo e problemas encontrados |
|---|---|---|---|
| Justiça em Números/CNJ | Estruturado - CSV | comparar o tempo médio até a sentença | 27 tribunais, ano de 2025, sem valores ausentes no arquivo processado. O dado é uma média por tribunal e não representa processos individuais |
| Notícias dos Juizados Especiais/CNJ | Não estruturado - HTML | apresentar informações de contexto | dez notícias coletadas. A estrutura da página pode mudar e exigir ajuste no notebook |
| CSV enviado pelo usuário | Estruturado - CSV | acrescentar observações sem alterar a base oficial | deve possuir as colunas `tribunal`, `observacao` e `fonte` |

## Campos utilizados

O arquivo `tempo_sentenca_juizados.csv` contém ano, tribunal, nome do tribunal, UF, tempo médio da sentença e quantidade de sentenças de conhecimento.

O arquivo `noticias_juizados.csv` contém título, data, resumo, URL e fonte da notícia.

Os dados estatísticos e as notícias são coletados em notebooks separados e salvos em `data/processed` para uso no aplicativo.
