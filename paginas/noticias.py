import streamlit as st
from comum import carregar_dados


_, noticias = carregar_dados()

st.title("Notícias dos Juizados Especiais")

st.write(
    "Conteúdo coletado da página de notícias dos Juizados Especiais no portal "
    "do CNJ com Beautiful Soup."
)

for _, noticia in noticias.head(5).iterrows():
    st.markdown(f"**{noticia['titulo']}**")
    st.caption(noticia["data"])
    st.write(noticia["resumo"])
    st.markdown(f"[Ler no portal do CNJ]({noticia['url']})")