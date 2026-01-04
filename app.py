import streamlit as st
import tempfile

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

from loaders import (
    carregar_site,
    carregar_youtube,
    carregar_pdf,
    carregar_csv,
    carregar_txt
)

from vectorstore import criar_vectorstore


# =============================
# CONFIGURAÇÕES
# =============================

TIPOS_ARQUIVOS = ["Site", "Youtube", "PDF", "Csv", "Txt"]

MODELOS = {
    "OpenAI": {
        "chat": ChatOpenAI,
        "modelos": ["gpt-4o-mini", "gpt-4o"]
    },
    "Groq": {
        "chat": ChatGroq,
        "modelos": [
            "llama-3.1-70b-versatile",
            "mixtral-8x7b-32768"
        ]
    }
}


# =============================
# FUNÇÕES AUXILIARES
# =============================

def carregar_arquivo(tipo, arquivo):
    if tipo == "Site":
        return carregar_site(arquivo)

    if tipo == "Youtube":
        return carregar_youtube(arquivo)

    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(arquivo.read())
        path = temp.name

    if tipo == "PDF":
        return carregar_pdf(path)

    if tipo == "Csv":
        return carregar_csv(path)

    if tipo == "Txt":
        return carregar_txt(path)


def inicializar_oraculo(provedor, modelo, api_key, tipo, arquivo):
    documento = carregar_arquivo(tipo, arquivo)

    vectordb = criar_vectorstore(documento, api_key)
    retriever = vectordb.as_retriever(search_kwargs={"k": 8})

    llm = MODELOS[provedor]["chat"](
        model=modelo,
        api_key=api_key,
        streaming=True
    )

    st.session_state.oraculo = {
        "retriever": retriever,
        "llm": llm
    }

    st.session_state.history = []
    st.success("✅ Oráculo inicializado com memória vetorial e streaming!")


def stream_resposta(oraculo, pergunta):
    retriever = oraculo["retriever"]
    llm = oraculo["llm"]

    docs = retriever.invoke(pergunta)

    contexto = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Você é um assistente chamado Oráculo.
Use SOMENTE as informações abaixo para responder.
Se não souber, diga que não encontrou no material.

###
{contexto}
###

Pergunta: {pergunta}
"""

    for chunk in llm.stream(prompt):
        yield chunk.content


# =============================
# INTERFACE
# =============================

st.set_page_config(
    page_title="Oráculo RAG",
    layout="wide"
)

st.title("🔮 Oráculo com Memória Vetorial (ChromaDB)")


# =============================
# SIDEBAR
# =============================

with st.sidebar:
    st.header("⚙️ Configurações")

    tipo = st.selectbox("Tipo de arquivo", TIPOS_ARQUIVOS)

    if tipo in ["Site", "Youtube"]:
        arquivo = st.text_input("URL")
    else:
        arquivo = st.file_uploader(
            "Upload de arquivo",
            type=tipo.lower()
        )

    provedor = st.selectbox("Provedor do modelo", MODELOS.keys())
    modelo = st.selectbox("Modelo", MODELOS[provedor]["modelos"])
    api_key = st.text_input("API Key", type="password")

    if st.button("🚀 Inicializar Oráculo"):
        if not arquivo or not api_key:
            st.error("Preencha todos os campos.")
        else:
            inicializar_oraculo(
                provedor,
                modelo,
                api_key,
                tipo,
                arquivo
            )

    if st.button("🧹 Limpar Memória"):
        st.session_state.history = []
        st.success("Memória limpa!")


# =============================
# CHAT
# =============================

if "oraculo" not in st.session_state:
    st.info("Inicialize o Oráculo no menu lateral.")
else:
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

        st.session_state.history.append(
            {"pergunta": pergunta, "resposta": resposta}
        )
