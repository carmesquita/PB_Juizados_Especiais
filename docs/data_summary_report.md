# Data Summary Report — TP2 Juizados Especiais

**Autora:** Carolina Gabriela Mesquita
**Versão:** 1.0 — 21/09/2026

## 1. Resumo das fontes

| Fonte | Tipo e cobertura | Campos usados | Objetivo e tratamento | Qualidade e limitações |
|---|---|---|---|---|
| Justiça em Números/CNJ, arquivo `23-jun-2026.zip` | CSV oficial; ano de referência 2025; 27 tribunais estaduais de 1º grau | `Tribunal`, `Cod.UF`, `Ano`, `Natureza`, `TpCorte`, `TpSentCJE` | filtrar Estadual, 1º Grau e `TpSentCJE`; renomear para nomes simples e salvar o CSV processado | 27 linhas, 27 tribunais/UF, sem nulos ou duplicatas no arquivo processado; é um agregado e não representa casos individuais |
| Página de notícias de Juizados Especiais do CNJ | HTML público; dez notícias mais recentes encontradas na execução | título, data, resumo e URL | salvar o HTML bruto e extrair os cartões com BeautifulSoup para CSV | dez URLs únicas e títulos preenchidos na execução; o HTML pode mudar e a notícia é apenas contexto |
| `data/sample/observacoes_exemplo.csv` / upload | CSV pequeno, complementar | `tribunal`, `uf`, `tempo_medio_sentenca_dias` | validar o cabeçalho antes de mostrar; manter separado da base oficial | depende do arquivo enviado pelo usuário; valores não são incorporados automaticamente à fonte oficial |

**Links das fontes:** [Justiça em Números/CNJ](https://www.cnj.jus.br/pesquisas-judiciarias/justica-em-numeros/), [notícias de Juizados Especiais](https://www.cnj.jus.br/programas-e-acoes/juizados-especiais/noticias/).

## 2. Dicionário dos dados processados

### `tempo_sentenca_juizados.csv`

- `tribunal`: sigla do Tribunal de Justiça;
- `uf`: unidade federativa;
- `ano`: ano de referência da estatística;
- `natureza`: natureza da Justiça, neste recorte `Estadual`;
- `tp_corte`: grau de jurisdição, neste recorte `1º Grau`;
- `tempo_medio_sentenca_dias`: média do tempo de sentença de conhecimento nos Juizados Especiais, em dias.

### `noticias_juizados.csv`

- `titulo`: título da notícia;
- `data`: data exibida na página;
- `resumo`: resumo apresentado no cartão;
- `url`: link da notícia no portal do CNJ.

### CSV complementar

O upload deve conter exatamente `tribunal`, `uf` e `tempo_medio_sentenca_dias`. Ele é mostrado em uma tabela separada para não misturar dados fornecidos pelo usuário com a base oficial.

## 3. Pipeline e rastreabilidade

1. O notebook estatístico baixa o ZIP oficial e guarda o snapshot em `data/raw` (o ZIP é ignorado pelo Git por ser grande).
2. O notebook de notícias baixa a página, grava `noticias_juizados.html` e extrai os dez cartões.
3. Os notebooks transformam as fontes e gravam os CSVs em `data/processed`.
4. `app.py` lê os CSVs processados, usa `st.cache_data` para a leitura e apresenta filtros, comparação, upload e download.

## 4. Verificações feitas

- o CSV de tempo tem 27 linhas, 27 tribunais/UF, sem valores ausentes e sem duplicatas;
- o CSV de notícias tem dez linhas, dez URLs únicas e títulos preenchidos;
- o aplicativo valida as colunas do upload e mostra uma mensagem de erro para esquema diferente;
- a coleta verifica o status HTTP e falha de forma explícita quando a página não responde;
- o `robots.txt` do CNJ foi consultado em 21/09/2026 e retornou `Allow: /` para o agente geral;
- uma tentativa de consultar a API padrão `/wp-json/` retornou 403; por isso o projeto documenta e usa a página HTML pública.

## 5. Limitações, licença e atualização

Os arquivos são retratos da data da execução. Uma nova coleta pode trazer outras notícias e atualizar o indicador. Antes de redistribuir o conteúdo, deve-se manter a atribuição ao CNJ e conferir as condições da fonte. A análise não faz inferência estatística, não mede causalidade e não substitui os relatórios oficiais.
