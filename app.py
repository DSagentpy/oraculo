import streamlit as st

from config import TIPOS_ARQUIVOS, MODELOS
from rag import inicializar_oraculo, stream_resposta
from session import remover_sessao


st.set_page_config(page_title="Oráculo RAG", layout="wide")
st.title("🔮 Oráculo com Memória Vetorial")

with st.sidebar:
    st.header("⚙️ Configurações")

    tipo = st.selectbox("Tipo de arquivo", TIPOS_ARQUIVOS)

    if tipo in ["Site", "Youtube"]:
        arquivo = st.text_input("URL")
    else:
        arquivo = st.file_uploader("Upload", type=tipo.lower())

    provedor = st.selectbox("Provedor", MODELOS.keys())
    modelo = st.selectbox("Modelo", MODELOS[provedor]["modelos"])
    api_key = st.text_input("API Key", type="password")

    if st.button("🚀 Inicializar Oráculo"):
        if not arquivo or not api_key:
            st.error("Preencha todos os campos.")
        else:
            inicializar_oraculo(provedor, modelo, api_key, tipo, arquivo)
            st.success("Oráculo inicializado!")

    if st.button("🧹 Limpar Histórico"):
        st.session_state.history = []

    if st.button("🗑️ Remover Sessão"):
        remover_sessao()
        st.success("Sessão removida!")


if "oraculo" not in st.session_state:
    st.info("Inicialize o Oráculo no menu lateral.")
else:
    for h in st.session_state.history:
        with st.chat_message("user"):
            st.markdown(h["pergunta"])

        with st.chat_message("assistant"):
            st.markdown(h["resposta"])

    pergunta = st.chat_input("Pergunte ao Oráculo")

    if pergunta:
        with st.chat_message("user"):
            st.markdown(pergunta)

        with st.chat_message("assistant"):
            resposta = st.write_stream(
                stream_resposta(
                    st.session_state.oraculo,
                    pergunta
                )
            )

        st.session_state.history.append({
            "pergunta": pergunta,
            "resposta": resposta
        })
