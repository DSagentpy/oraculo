from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

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

MAX_HISTORICO = 4 #limite de mensagens no histórico
