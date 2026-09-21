# Project Charter — TP2 Juizados Especiais

**Autora:** Carolina Gabriela Mesquita
**Versão:** 1.0 — 21/09/2026

## 1. Problema e pergunta

O tempo de sentença pode variar entre os Tribunais de Justiça. Neste trabalho eu organizo o indicador do CNJ e faço uma comparação simples entre os 27 tribunais estaduais.

**Pergunta:** quais tribunais apresentam os maiores e os menores tempos médios de sentença de conhecimento nos Juizados Especiais e como o usuário pode explorar essa diferença?

## 2. Objetivos

**Objetivo geral:** criar uma aplicação simples e reproduzível para explorar o tempo médio de sentença por tribunal.

**Objetivos específicos:**

- extrair e documentar o indicador da base Justiça em Números;
- apresentar a média, o menor e o maior valor;
- permitir filtro por limite de dias, seleção de tribunais e comparação;
- permitir baixar os dados filtrados e carregar um CSV complementar;
- mostrar notícias do CNJ para dar contexto ao indicador;
- separar a coleta da interface e deixar as etapas registradas no TDSP.

## 3. Escopo

**Dentro do escopo:** os 27 Tribunais de Justiça estaduais, o indicador `TpSentCJE` (média), o ano disponível na extração, notícias da página de Juizados Especiais do CNJ e um CSV complementar com as mesmas colunas.

**Fora do escopo:** processos individuais, previsão de duração, comparação com tribunais federais ou trabalhistas, avaliação de produtividade de pessoas e interpretação causal das notícias.

## 4. Público e uso

O público é formado por alunos, professor e pessoas interessadas em dados públicos de Justiça. A tela foi pensada para uma consulta rápida: escolher um limite, selecionar tribunais, ver o gráfico/tabela e baixar o resultado.

## 5. Fontes e método

1. **Justiça em Números/CNJ:** arquivo CSV dentro do ZIP oficial. O notebook `extrair_justica_em_numeros.ipynb` baixa o snapshot, filtra `Ano=2025`, `Natureza=Estadual` e `TpCorte=1º Grau`, seleciona `TpSentCJE` e grava `data/processed/tempo_sentenca_juizados.csv`.
2. **Notícias do CNJ:** página pública de Juizados Especiais. O notebook `coletar_noticias_juizados.ipynb` verifica a resposta, salva o HTML bruto e extrai título, data, resumo e URL com BeautifulSoup.
3. **Upload do usuário:** CSV complementar validado na aplicação antes de ser exibido.

## 6. Indicadores de sucesso e aceite

- carregar os 27 tribunais sem valores ausentes ou duplicados;
- exibir média, mínimo e máximo em dias;
- filtrar e ordenar os tribunais;
- selecionar tribunais e manter a comparação em `st.session_state`;
- baixar o recorte em CSV e aceitar um arquivo complementar;
- exibir as notícias coletadas;
- usar cache para os dados e executar a interface com `streamlit run app.py`;
- reproduzir a instalação com os arquivos de requisitos e os notebooks com o kernel documentado.

## 7. Riscos e respostas

| Risco | Resposta |
|---|---|
| O CNJ mudar o HTML ou o nome de uma coluna | manter snapshots em `data/raw`, testar seletores/colunas e registrar a data da extração |
| A internet estar indisponível | usar os CSVs processados já versionados para a interface |
| O indicador agregado ser interpretado como caso individual | explicar a limitação na tela e neste documento |
| Upload com colunas erradas | validar exatamente `tribunal`, `uf` e `tempo_medio_sentenca_dias` |
| Caminhos diferentes em outro computador | usar `Path.cwd()`, instruir a execução pela raiz e documentar o kernel |
| O repositório ficar pesado | não versionar o `.venv` nem o ZIP bruto grande |

## 8. Entregas e etapas TDSP

- `src/extrair_justica_em_numeros.ipynb`: extração e transformação estatística;
- `src/coletar_noticias_juizados.ipynb`: coleta HTML com BeautifulSoup;
- `data/raw/` e `data/processed/`: evidências da coleta e arquivos consumidos;
- `app.py`: interface, cache, estado, upload e download;
- `docs/`: este Charter e o Data Summary Report;
- `README.md`, `requirements*.txt` e `.gitignore`: reprodução e publicação;
- `tdsp/`: planejamento, exploração, preparação, modelagem/apresentação e conclusão.

## 9. Limitações e transparência

O valor mostrado é uma média por tribunal. O indicador não permite inferir a duração de um processo específico nem uma causa para a diferença entre tribunais. O cálculo da tela é uma média simples dos valores dos tribunais; os dados de notícias não alteram essa conta.

Usei as aulas, a documentação das bibliotecas e auxílio do ChatGPT para revisar código e organizar os documentos. A autoria das decisões, dos testes e da conferência dos resultados é minha.
