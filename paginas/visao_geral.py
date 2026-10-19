import streamlit as st

from comum import carregar_dados


dados, _ = carregar_dados()

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

coluna1, coluna2, coluna3, coluna4 = st.columns(4)

with coluna1:
    st.metric("Tribunais analisados", len(dados))

with coluna2:
    st.metric(
        "Média dos tribunais",
        f"{dados['tempo_medio_sentenca_dias'].mean():.1f} dias",
    )

with coluna3:
    st.metric(
        "Menor tempo",
        f"{dados.iloc[0]['tribunal']} — "
        f"{dados.iloc[0]['tempo_medio_sentenca_dias']:.1f} dias",
    )

with coluna4:
    st.metric(
        "Maior tempo",
        f"{dados.iloc[-1]['tribunal']} — "
        f"{dados.iloc[-1]['tempo_medio_sentenca_dias']:.1f} dias",
    )

st.subheader("Fontes")

st.markdown(
    "- [Justiça em Números](https://www.cnj.jus.br/justica-em-numeros/)\n"
    "- [Notícias dos Juizados Especiais]"
    "(https://www.cnj.jus.br/programas-e-acoes/juizados-especiais/noticias/)\n"
    "- [ODS 16](https://brasil.un.org/pt-br/sdgs/16)"
)

st.caption(
    "O indicador é agregado por tribunal e não permite avaliar processos ou "
    "unidades judiciais individualmente."
)