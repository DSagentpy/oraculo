import streamlit as st
import uuid #gerar um id único para cada mensagem
import shutil #copiar arquivos temporários para o diretório de saída
import os 

def criar_sessao():
    session_id = str(uuid.uuid4())
    persist_dir = f"./chromadb/{session_id}"
    return persist_dir


def remover_sessao():
    if "oraculo" in st.session_state:
        persist_dir = st.session_state.oraculo.get("persist_dir")

        if persist_dir and os.path.exists(persist_dir):
            shutil.rmtree(persist_dir)

    st.session_state.pop("oraculo", None)
    st.session_state.pop("history", None)