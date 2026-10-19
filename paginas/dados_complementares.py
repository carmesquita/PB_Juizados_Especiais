import pandas as pd
import requests
import streamlit as st

from comum import (
    CAMPOS_COMPLEMENTARES,
    carregar_dados,
    iniciar_estado,
)


URL_API = "http://127.0.0.1:8000"

dados, _ = carregar_dados()
iniciar_estado()

st.title("Dados complementares")

st.write(
    "As informações complementares podem ser enviadas pela API "
    "ou por meio de um arquivo CSV."
)

st.subheader("Enviar pela API")

with st.form("formulario_api"):
    tribunal = st.selectbox(
        "Tribunal",
        sorted(dados["tribunal"]),
    )

    observacao = st.text_area(
        "Observação",
        placeholder="Digite uma informação complementar.",
    )

    fonte = st.text_input(
        "Fonte",
        placeholder="Informe a origem da informação.",
    )

    enviar = st.form_submit_button("Enviar observação")

if enviar:
    observacao = observacao.strip()
    fonte = fonte.strip()

    if len(observacao) < 5 or len(fonte) < 2:
        st.error("Preencha a observação e a fonte.")
    else:
        try:
            resposta = requests.post(
                f"{URL_API}/observacoes",
                json={
                    "tribunal": tribunal,
                    "observacao": observacao,
                    "fonte": fonte,
                },
                timeout=10,
            )

            if resposta.status_code == 201:
                registro = resposta.json()

                nova_linha = pd.DataFrame(
                    [
                        {
                            "tribunal": registro["tribunal"],
                            "observacao": registro["observacao"],
                            "fonte": registro["fonte"],
                        }
                    ]
                )

                st.session_state["dados_complementares"] = pd.concat(
                    [
                        st.session_state["dados_complementares"],
                        nova_linha,
                    ],
                    ignore_index=True,
                )

                st.success(
                    f"Observação enviada pela API. "
                    f"Identificador: {registro['id']}."
                )
            else:
                detalhe = resposta.json().get(
                    "detail",
                    "Erro não identificado.",
                )
                st.error(
                    f"A API retornou o erro "
                    f"{resposta.status_code}: {detalhe}"
                )

        except requests.RequestException:
            st.error(
                "Não foi possível conectar à API. "
                "Verifique se o FastAPI está em execução."
            )

st.divider()
st.subheader("Enviar arquivo CSV")

st.write(
    "O arquivo deve possuir as colunas: tribunal, observacao e fonte. "
    "Um modelo está disponível na pasta data/sample."
)

arquivo = st.file_uploader(
    "Adicionar arquivo CSV",
    type="csv",
)

if arquivo is not None and st.button("Carregar arquivo"):
    complemento = pd.read_csv(arquivo, dtype="string")

    if list(complemento.columns) == CAMPOS_COMPLEMENTARES:
        st.session_state["dados_complementares"] = pd.concat(
            [
                st.session_state["dados_complementares"],
                complemento,
            ],
            ignore_index=True,
        )
        st.success("Arquivo adicionado.")
    else:
        st.error("O cabeçalho do arquivo está diferente do modelo.")

if not st.session_state["dados_complementares"].empty:
    st.subheader("Informações adicionadas")

    st.dataframe(
        st.session_state["dados_complementares"],
        hide_index=True,
    )

    st.download_button(
        "Baixar dados complementares",
        st.session_state["dados_complementares"]
        .to_csv(index=False)
        .encode("utf-8-sig"),
        "dados_complementares.csv",
        "text/csv",
    )