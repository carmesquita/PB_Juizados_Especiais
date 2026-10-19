import streamlit as st

from comum import iniciar_estado


# projeto feito com auxilio de IA Chat GPT

st.set_page_config(
    page_title="Tempo de sentença nos Juizados Especiais",
    layout="wide",
)

iniciar_estado()

paginas = [
    st.Page(
        "paginas/visao_geral.py",
        title="Visão geral",
        default=True,
    ),
    st.Page(
        "paginas/comparacao.py",
        title="Comparação entre tribunais",
    ),
    st.Page(
        "paginas/noticias.py",
        title="Notícias",
    ),
    st.Page(
        "paginas/dados_complementares.py",
        title="Dados complementares",
    ),
]

pagina_selecionada = st.navigation(paginas)
pagina_selecionada.run()