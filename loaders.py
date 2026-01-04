from langchain_community.document_loaders import (
    WebBaseLoader,
    YoutubeLoader,
    PyPDFLoader,
    CSVLoader,
    TextLoader
)

import os
from fake_useragent import UserAgent
import streamlit as st
from time import sleep

def carregar_site(url):
    documento = ''
    for i in range(5):
        try:
            os.environ['USER_AGENT'] = UserAgent().random
            loader = WebBaseLoader(url, raise_for_status=True)
            docs = loader.load()
            documento = '\n\n'.join([doc.page_content for doc in docs])
            break
        except:
            sleep(3)

    if documento == '':
        st.error("Não foi possível carregar o site")
        st.stop()

    return documento

def carregar_youtube(url):
    loader = YoutubeLoader.from_youtube_url(
        url,
        add_video_info=False,
        language=["pt"]
    )
    docs = loader.load()
    return '\n\n'.join([doc.page_content for doc in docs])

def carregar_csv(caminho_csv):
    loader = CSVLoader(caminho_csv)
    docs = loader.load()
    return '\n\n'.join([doc.page_content for doc in docs])

def carregar_pdf(caminho_pdf):
    loader = PyPDFLoader(caminho_pdf)
    docs = loader.load()
    return '\n\n'.join([doc.page_content for doc in docs])

def carregar_txt(caminho_txt):
    loader = TextLoader(caminho_txt)
    docs = loader.load()
    return '\n\n'.join([doc.page_content for doc in docs])
