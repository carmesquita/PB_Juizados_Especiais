from functools import lru_cache
from pathlib import Path

import pandas as pd
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


PASTA_PROJETO = Path(__file__).resolve().parent.parent
ARQUIVO_TRIBUNAIS = (
    PASTA_PROJETO
    / "data"
    / "processed"
    / "tempo_sentenca_juizados.csv"
)


class Tribunal(BaseModel):
    ano: int
    tribunal: str
    nome_tribunal: str
    uf: str
    tempo_medio_sentenca_dias: float
    sentencas_conhecimento: int


class ObservacaoEntrada(BaseModel):
    tribunal: str = Field(min_length=2, max_length=10)
    observacao: str = Field(min_length=5, max_length=500)
    fonte: str = Field(min_length=2, max_length=200)


class ObservacaoResposta(ObservacaoEntrada):
    id: int


app = FastAPI(
    title="API dos Juizados Especiais",
    description=(
        "API para consulta dos dados dos Tribunais de Justiça e "
        "recebimento de informações complementares."
    ),
    version="1.0.0",
)

observacoes: list[ObservacaoResposta] = []


@lru_cache
def carregar_tribunais() -> pd.DataFrame:
    return pd.read_csv(ARQUIVO_TRIBUNAIS)


@app.get(
    "/",
    tags=["Status"],
    summary="Apresentar informações da API",
)
def inicio():
    return {
        "mensagem": "API dos Juizados Especiais em funcionamento.",
        "documentacao": "/docs",
    }


@app.get(
    "/tribunais",
    response_model=list[Tribunal],
    tags=["Tribunais"],
    summary="Listar todos os tribunais",
)
def listar_tribunais():
    dados = carregar_tribunais()
    return dados.to_dict(orient="records")


@app.get(
    "/tribunais/{sigla}",
    response_model=Tribunal,
    tags=["Tribunais"],
    summary="Consultar um tribunal pela sigla",
)
def consultar_tribunal(sigla: str):
    dados = carregar_tribunais()
    sigla = sigla.strip().upper()

    resultado = dados.loc[dados["tribunal"] == sigla]

    if resultado.empty:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tribunal não encontrado.",
        )

    return resultado.iloc[0].to_dict()


@app.post(
    "/observacoes",
    response_model=ObservacaoResposta,
    status_code=status.HTTP_201_CREATED,
    tags=["Observações"],
    summary="Receber uma informação complementar",
)
def criar_observacao(observacao: ObservacaoEntrada):
    tribunal = observacao.tribunal.strip().upper()
    texto = observacao.observacao.strip()
    fonte = observacao.fonte.strip()

    if not texto or not fonte:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A observação e a fonte não podem ficar vazias.",
        )

    dados = carregar_tribunais()

    if tribunal not in dados["tribunal"].values:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tribunal não encontrado.",
        )

    registro = ObservacaoResposta(
        id=len(observacoes) + 1,
        tribunal=tribunal,
        observacao=texto,
        fonte=fonte,
    )

    observacoes.append(registro)
    return registro