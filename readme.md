# PB Juizados Especiais — TP3

Projeto acadêmico sobre o tempo médio até a sentença nos Juizados Especiais dos 27 Tribunais de Justiça estaduais.

O TP3 dá continuidade ao projeto anterior, mantendo os dados e funcionalidades existentes e acrescentando uma aplicação multipáginas, uma API com FastAPI e a preparação dos textos das notícias para uso futuro com LLMs.

## Funcionalidades

- visão geral dos dados;
- comparação e consulta entre tribunais;
- gráfico, tabela, filtros e download de CSV;
- apresentação de notícias coletadas do portal do CNJ;
- envio de dados complementares por CSV;
- envio de observações pela API;
- rotas GET e POST documentadas pelo FastAPI;
- arquivo textual preparado para uso futuro com LLMs.

## Estrutura

- `app.py`: entrada e navegação do Streamlit;
- `paginas/`: páginas da aplicação;
- `api/`: API desenvolvida com FastAPI;
- `data/`: arquivos brutos, processados e de exemplo;
- `src/`: notebooks de coleta e preparação;
- `docs/`: Project Charter e Data Summary Report.

## Instalação

Crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install -r requirements-api.txt
```

## Execução

Inicie a API em um terminal:

```powershell
python -m uvicorn api.main:app --reload
```

A documentação ficará disponível em:

```text
http://127.0.0.1:8000/docs
```

Em outro terminal, inicie o Streamlit:

```powershell
python -m streamlit run app.py
```

A aplicação ficará disponível em:

```text
http://localhost:8501
```

A API deve permanecer em execução para que o formulário de envio de observações funcione. As observações recebidas são temporárias e não alteram a base oficial.

## Fontes

- Conselho Nacional de Justiça — Justiça em Números;
- portal de notícias dos Juizados Especiais;
- Organização das Nações Unidas — ODS 16.

## Autoria

Carolina Gabriela Mesquita.

Projeto desenvolvido para fins acadêmicos, com apoio de ferramentas de inteligência artificial na organização, revisão e desenvolvimento de partes do código.