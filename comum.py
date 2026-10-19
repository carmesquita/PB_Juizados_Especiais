from pathlib import Path

import pandas as pd
import streamlit as st


PASTA_PROJETO = Path(__file__).resolve().parent
CAMPOS_COMPLEMENTARES = ["tribunal", "observacao", "fonte"]


@st.cache_data
def carregar_dados():
    dados = pd.read_csv(
        PASTA_PROJETO
        / "data"
        / "processed"
        / "tempo_sentenca_juizados.csv"
    )

    noticias = pd.read_csv(
        PASTA_PROJETO
        / "data"
        / "processed"
        / "noticias_juizados.csv"
    )

    return dados, noticias


def iniciar_estado():
    st.session_state.setdefault("comparacao", [])
    st.session_state.setdefault(
        "dados_complementares",
        pd.DataFrame(columns=CAMPOS_COMPLEMENTARES),
    )
    st.session_state.setdefault("limite", 420)
    st.session_state.setdefault("ordem", "Menor tempo primeiro")