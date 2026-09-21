from pathlib import Path

import pandas as pd
import streamlit as st

#projeto feito com auxilio de IA Chat GPT
PASTA_PROJETO = Path(__file__).resolve().parent
CAMPOS_COMPLEMENTARES = ["tribunal", "observacao", "fonte"]

st.set_page_config(
    page_title="Tempo de sentença nos Juizados Especiais",
    page_icon=":material/balance:",
    layout="wide",
)


@st.cache_data
def carregar_dados():
    return (
        pd.read_csv(PASTA_PROJETO / "data" / "processed" / "tempo_sentenca_juizados.csv"),
        pd.read_csv(PASTA_PROJETO / "data" / "processed" / "noticias_juizados.csv"),
    )


dados, noticias = carregar_dados()
st.session_state.setdefault("comparacao", [])
st.session_state.setdefault(
    "dados_complementares",
    pd.DataFrame(columns=CAMPOS_COMPLEMENTARES),
)

st.title("Tempo de sentença nos Juizados Especiais Estaduais")
st.write(
    "O painel compara o tempo médio até a sentença na fase de conhecimento dos "
    "Juizados Especiais dos 27 Tribunais de Justiça. O tema está relacionado "
    "ao acesso à Justiça e à eficiência institucional previstos na ODS 16."
)
st.caption(
    "Dados de 2025 da base Justiça em Números, publicada pelo Conselho Nacional "
    "de Justiça em 2026."
)

with st.container(horizontal=True):
    st.metric("Tribunais analisados", len(dados), border=True)
    st.metric(
        "Média dos tribunais",
        f"{dados['tempo_medio_sentenca_dias'].mean():.1f} dias",
        border=True,
    )
    st.metric(
        "Menor tempo",
        f"{dados.iloc[0]['tribunal']} — {dados.iloc[0]['tempo_medio_sentenca_dias']:.1f} dias",
        border=True,
    )
    st.metric(
        "Maior tempo",
        f"{dados.iloc[-1]['tribunal']} — {dados.iloc[-1]['tempo_medio_sentenca_dias']:.1f} dias",
        border=True,
    )

st.header("Comparação entre tribunais", icon=":material/bar_chart:")

coluna1, coluna2 = st.columns(2)
limite = coluna1.slider(
    "Mostrar tribunais com tempo de até",
    min_value=90,
    max_value=420,
    value=420,
    step=10,
    format="%d dias",
)
ordem = coluna2.selectbox(
    "Ordenar o resultado",
    ["Menor tempo primeiro", "Maior tempo primeiro"],
)

filtrados = dados.loc[dados["tempo_medio_sentenca_dias"] <= limite].copy()
filtrados = filtrados.sort_values(
    "tempo_medio_sentenca_dias",
    ascending=ordem == "Menor tempo primeiro",
)

st.bar_chart(
    filtrados,
    x="tribunal",
    y="tempo_medio_sentenca_dias",
    x_label="Tribunal",
    y_label="Tempo médio em dias",
)

st.dataframe(
    filtrados[
        [
            "tribunal",
            "uf",
            "tempo_medio_sentenca_dias",
            "sentencas_conhecimento",
        ]
    ].rename(
        columns={
            "tribunal": "Tribunal",
            "uf": "UF",
            "tempo_medio_sentenca_dias": "Tempo médio da sentença",
            "sentencas_conhecimento": "Sentenças de conhecimento",
        }
    ),
    hide_index=True,
    column_config={
        "Tempo médio da sentença": st.column_config.NumberColumn(format="%.1f dias"),
        "Sentenças de conhecimento": st.column_config.NumberColumn(format="%d"),
    },
)

st.download_button(
    "Baixar dados filtrados",
    filtrados.to_csv(index=False).encode("utf-8-sig"),
    "tempo_sentenca_juizados.csv",
    "text/csv",
    icon=":material/download:",
)

st.subheader("Consulta e comparação")
tribunal_selecionado = st.selectbox(
    "Selecione um tribunal",
    sorted(dados["tribunal"]),
)
linha_selecionada = dados.loc[dados["tribunal"] == tribunal_selecionado].iloc[0]

with st.container(horizontal=True):
    st.metric(
        f"Tempo no {tribunal_selecionado}",
        f"{linha_selecionada['tempo_medio_sentenca_dias']:.1f} dias",
        border=True,
    )
    st.metric(
        "Sentenças de conhecimento",
        f"{linha_selecionada['sentencas_conhecimento']:,.0f}".replace(",", "."),
        border=True,
    )

if st.button("Adicionar à comparação", icon=":material/add:"):
    if tribunal_selecionado not in st.session_state["comparacao"]:
        st.session_state["comparacao"].append(tribunal_selecionado)

if st.session_state["comparacao"]:
    st.dataframe(
        dados.loc[
            dados["tribunal"].isin(st.session_state["comparacao"]),
            ["tribunal", "tempo_medio_sentenca_dias", "sentencas_conhecimento"],
        ],
        hide_index=True,
    )
    if st.button("Limpar comparação", icon=":material/delete:"):
        st.session_state["comparacao"].clear()
        st.rerun()

st.header("Notícias dos Juizados Especiais", icon=":material/newspaper:")
st.write(
    "Conteúdo coletado da página de notícias dos Juizados Especiais no portal "
    "do CNJ com Beautiful Soup."
)

for _, noticia in noticias.head(5).iterrows():
    with st.container(border=True):
        st.markdown(f"**{noticia['titulo']}**")
        st.caption(noticia["data"])
        st.write(noticia["resumo"])
        st.markdown(f"[Ler no portal do CNJ]({noticia['url']})")

st.header("Dados complementares", icon=":material/upload_file:")
st.write(
    "O arquivo deve possuir as colunas: tribunal, observacao e fonte. Um modelo "
    "está disponível na pasta data/sample."
)

arquivo = st.file_uploader("Adicionar arquivo CSV", type="csv")

if arquivo is not None and st.button("Carregar arquivo"):
    complemento = pd.read_csv(arquivo, dtype="string")
    if list(complemento.columns) == CAMPOS_COMPLEMENTARES:
        st.session_state["dados_complementares"] = pd.concat(
            [st.session_state["dados_complementares"], complemento],
            ignore_index=True,
        )
        st.success("Arquivo adicionado.")
    else:
        st.error("O cabeçalho do arquivo está diferente do modelo.")

if not st.session_state["dados_complementares"].empty:
    st.dataframe(st.session_state["dados_complementares"], hide_index=True)
    st.download_button(
        "Baixar dados complementares",
        st.session_state["dados_complementares"].to_csv(index=False).encode("utf-8-sig"),
        "dados_complementares.csv",
        "text/csv",
        icon=":material/download:",
    )

st.subheader("Fontes")
st.markdown(
    "- [Justiça em Números](https://www.cnj.jus.br/justica-em-numeros/)\n"
    "- [Notícias dos Juizados Especiais](https://www.cnj.jus.br/programas-e-acoes/juizados-especiais/noticias/)\n"
    "- [ODS 16](https://brasil.un.org/pt-br/sdgs/16)"
)
st.caption(
    "O indicador é agregado por tribunal e não permite avaliar processos ou "
    "unidades judiciais individualmente."
)
