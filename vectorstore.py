from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings


def criar_vectorstore(documento, api_key):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=500
    )

    textos = splitter.split_text(documento)

    embeddings = OpenAIEmbeddings(
        api_key=api_key
    )

    vectordb = Chroma.from_texts(
        texts=textos,
        embedding=embeddings,
        persist_directory="./chromadb"
    )

    return vectordb
