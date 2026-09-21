# TP2 — Juizados Especiais

Aplicação desenvolvida para o Projeto de Bloco. O objetivo é comparar o tempo médio, em dias, das sentenças de conhecimento nos Juizados Especiais dos 27 Tribunais de Justiça estaduais. A aplicação também apresenta notícias do CNJ como contexto e permite incluir um CSV complementar.

## Como executar

No PowerShell, a partir desta pasta:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pip install -r requirements-dev.txt
python -m ipykernel install --user --name tp2-juizados --display-name "Python (TP2 Juizados)"
streamlit run app.py
```

Para executar os notebooks, abra a pasta no JupyterLab ou VS Code e selecione o kernel **Python (TP2 Juizados)**. Eles procuram a pasta `data` na pasta atual e nas pastas acima, portanto não dependem do caminho do computador de quem executa.

O `requirements.txt` contém somente as dependências da aplicação. O `requirements-dev.txt` acrescenta as ferramentas usadas nos notebooks, deixando a instalação do Streamlit Community Cloud mais simples.

## Organização

- `app.py`: interface Streamlit;
- `src/`: notebooks de extração, separados da interface;
- `data/raw/`: snapshots baixados das fontes (o ZIP grande é ignorado pelo Git);
- `data/processed/`: CSVs utilizados pela aplicação;
- `data/sample/`: exemplo de CSV para upload;
- `docs/`: Project Charter e Data Summary Report;
- `tdsp/`: registros das etapas do TDSP/CRISP-DM.

## Fontes e cuidados

Os dados estatísticos vêm do portal Justiça em Números/CNJ. As notícias são coletadas da página de Juizados Especiais do CNJ com `requests` e BeautifulSoup, fora do aplicativo. O `robots.txt` consultado em 21/09/2026 permite o acesso geral (`Allow: /`); a aplicação mantém a atribuição da fonte. A API padrão `/wp-json/` do portal retornou 403 no teste, por isso a coleta usa a página HTML pública.

O indicador é agregado por tribunal e representa uma média; não descreve processos individuais. As notícias servem como contexto e não entram no cálculo estatístico.

## Git, GitHub e publicação

O projeto possui histórico local. Depois de criar um repositório no GitHub, configure o remoto e envie a branch `main`:

```powershell
git remote add origin <URL-do-repositorio>
git push -u origin main
```

URL do GitHub: **a preencher após a criação do repositório**.

Depois do push, no Streamlit Community Cloud escolha o repositório, a branch `main` e o arquivo `app.py`. URL do aplicativo: **a preencher após a publicação**.

Não coloque `.venv`, tokens ou senhas no repositório. O arquivo `.gitignore` já exclui esses itens.

## Transparência

Usei as aulas, a documentação das bibliotecas e auxílio do ChatGPT para revisar trechos e organizar a documentação. A seleção das fontes, os testes e a conferência dos resultados foram feitos no projeto.
