import streamlit as st
import tempfile

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from loaders import (
    carregar_site,
    carregar_youtube,
    carregar_pdf,
    carregar_csv,
    carregar_txt
)

# =============================
# CONFIGURAÇÕES
# =============================

TIPOS_ARQUIVOS_VALIDOS = ["Site", "Youtube", "PDF", "Csv", "Txt"]

CONFIG_MODELOS = {
    "OpenAI": {
        "modelo": ["gpt-4o-mini", "gpt-4o"],
        "chat": ChatOpenAI,
    },
    "Groq": {
        "modelo": [
            "llama-3.1-70b-versatile",
            "gemma2-9b-it",
            "mixtral-8x7b-32768"
        ],
        "chat": ChatGroq,
    }
}

# =============================
# ESTADO GLOBAL (Streamlit)
# =============================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# =============================
# CARREGAMENTO DE ARQUIVOS
# =============================

def carregar_arquivo(tipo_arquivo, arquivo):
    if tipo_arquivo == "Site":
        return carregar_site(arquivo)

    if tipo_arquivo == "Youtube":
        return carregar_youtube(arquivo)

    if tipo_arquivo == "PDF":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
            temp.write(arquivo.read())
            temp_path = temp.name
        return carregar_pdf(temp_path)

    if tipo_arquivo == "Csv":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp:
            temp.write(arquivo.read())
            temp_path = temp.name
        return carregar_csv(temp_path)

    if tipo_arquivo == "Txt":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp:
            temp.write(arquivo.read())
            temp_path = temp.name
        return carregar_txt(temp_path)

    return None

# =============================
# INICIALIZA O MODELO
# =============================

def carregar_modelo(provedor, modelo, api_key, tipo_arquivo, arquivo):
    documento = carregar_arquivo(tipo_arquivo, arquivo)

    system_message = f"""
Você é um assistente amigável chamado Oráculo.

Você possui acesso às seguintes informações vindas de um documento do tipo {tipo_arquivo}:

###
{documento}
###

Use SOMENTE essas informações para responder.
Se aparecer "$", substitua por "s".
Se o conteúdo parecer bloqueado por JavaScript, sugira recarregar o Oráculo.
"""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_message),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])

    chat = CONFIG_MODELOS[provedor]["chat"](
        model=modelo,
        api_key=api_key
    )

    st.session_state.chat = prompt | chat
    st.success("✅ Oráculo inicializado com sucesso!")

# =============================
# PÁGINA DE CHAT
# =============================

def pagina_chat():
    st.header("🤖 Bem-vindo ao Oráculo", divider=True)

    if "chat" not in st.session_state:
        st.warning("Inicialize o Oráculo pelo menu lateral.")
        return

    # Exibir histórico
    for msg in st.session_state.chat_history:
        role = "human" if isinstance(msg, HumanMessage) else "ai"
        with st.chat_message(role):
            st.markdown(msg.content)

    pergunta = st.chat_input("Fale com o Oráculo")

    if pergunta:
        with st.chat_message("human"):
            st.markdown(pergunta)

        resposta = st.session_state.chat.invoke({
            "input": pergunta,
            "chat_history": st.session_state.chat_history
        })

        with st.chat_message("ai"):
            st.markdown(resposta.content)

        st.session_state.chat_history.append(HumanMessage(content=pergunta))
        st.session_state.chat_history.append(AIMessage(content=resposta.content))

# =============================
# SIDEBAR
# =============================

def sidebar():
    tabs = st.tabs(["Upload de Arquivo", "Modelos"])

    with tabs[0]:
        tipo_arquivo = st.selectbox(
            "Selecione o tipo de arquivo",
            TIPOS_ARQUIVOS_VALIDOS
        )

        if tipo_arquivo in ["Site", "Youtube"]:
            arquivo = st.text_input("Digite a URL")
        else:
            extensao = tipo_arquivo.lower()
            arquivo = st.file_uploader(
                f"Upload de arquivo ({extensao})",
                type=extensao
            )

    with tabs[1]:
        provedor = st.selectbox(
            "Provedor do modelo",
            CONFIG_MODELOS.keys()
        )

        modelo = st.selectbox(
            "Modelo",
            CONFIG_MODELOS[provedor]["modelo"]
        )

        api_key = st.text_input(
            f"API Key ({provedor})",
            type="password"
        )

    if st.button("🚀 Inicializar Oráculo"):
        if not arquivo or not api_key:
            st.error("Preencha todos os campos.")
            return

        st.session_state.chat_history = []

        carregar_modelo(
            provedor,
            modelo,
            api_key,
            tipo_arquivo,
            arquivo
        )

    if st.button("🧹 Limpar Memória"):
        st.session_state.chat_history = []
        st.success("Memória limpa com sucesso!")

# =============================
# MAIN
# =============================

def main():
    with st.sidebar:
        sidebar()
    pagina_chat()

if __name__ == "__main__":
    main()
