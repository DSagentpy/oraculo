# 🤖 Oráculo

Oráculo é uma aplicação web interativa construída com Streamlit que permite conversar com modelos de IA (OpenAI e Groq) sobre diferentes tipos de documentos. Você pode fazer upload de arquivos ou fornecer URLs e fazer perguntas sobre o conteúdo usando assistentes de IA.

## ✨ Funcionalidades

- **Múltiplos tipos de documentos suportados:**
  - 📄 Sites (URLs)
  - 🎥 Vídeos do YouTube
  - 📑 Arquivos PDF
  - 📊 Arquivos CSV
  - 📝 Arquivos de texto (TXT)

- **Múltiplos provedores de IA:**
  - OpenAI (GPT-4o, GPT-4o-mini)
  - Groq (Llama 3.1 70B, Gemma2 9B, Mixtral 8x7B)

- **Interface intuitiva:**
  - Chat interativo com histórico de conversas
  - Sidebar para configuração e upload
  - Limpeza de memória do chat

## 📋 Pré-requisitos

- Python 3.8 ou superior
- API Keys:
  - OpenAI API Key (para modelos OpenAI)
  - Groq API Key (para modelos Groq)

## 🚀 Instalação

1. Clone o repositório ou navegue até o diretório do projeto:
```bash
cd oraculo
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 📦 Dependências

O projeto utiliza as seguintes bibliotecas principais:

- `streamlit` - Framework para aplicações web
- `langchain` - Framework para aplicações com LLMs
- `langchain-community` - Loaders de documentos da comunidade
- `langchain-groq` - Integração com Groq
- `langchain-openai` - Integração com OpenAI
- `fake_useragent` - Geração de User-Agents aleatórios
- `pypdf` - Processamento de PDFs
- `bs4` - Parsing de HTML

## 🎯 Como Usar

1. **Inicie a aplicação:**
```bash
streamlit run 03_aula.py
```

2. **Configure o Oráculo:**
   - Na sidebar, vá para a aba "Upload de Arquivo"
   - Selecione o tipo de arquivo (Site, Youtube, PDF, Csv ou Txt)
   - Forneça a URL ou faça upload do arquivo
   - Vá para a aba "Modelos"
   - Selecione o provedor (OpenAI ou Groq)
   - Escolha o modelo desejado
   - Insira sua API Key
   - Clique em "🚀 Inicializar Oráculo"

3. **Comece a conversar:**
   - Digite suas perguntas no campo de chat
   - O Oráculo responderá com base no conteúdo do documento carregado
   - Use "🧹 Limpar Memória" para resetar o histórico de conversas

## 📁 Estrutura do Projeto

```
oraculo/
├── 03_aula.py          # Aplicação principal Streamlit
├── loaders.py          # Funções para carregar diferentes tipos de documentos
├── opcao.py            # Exemplo de uso do PlaywrightURLLoader
├── requirements.txt    # Dependências do projeto
└── README.md           # Este arquivo
```

## 🔧 Arquivos Principais

### `03_aula.py`
Aplicação principal que contém:
- Interface Streamlit
- Gerenciamento de estado (histórico de chat)
- Inicialização de modelos de IA
- Interface de chat interativa

### `loaders.py`
Módulo com funções para carregar diferentes tipos de documentos:
- `carregar_site()` - Carrega conteúdo de URLs
- `carregar_youtube()` - Extrai transcrições de vídeos do YouTube
- `carregar_pdf()` - Processa arquivos PDF
- `carregar_csv()` - Processa arquivos CSV
- `carregar_txt()` - Processa arquivos de texto

### `opcao.py`
Exemplo de uso alternativo do `PlaywrightURLLoader` para carregar conteúdo de sites.

## 💡 Exemplos de Uso

### Carregar um site
1. Selecione "Site" como tipo de arquivo
2. Digite a URL: `https://exemplo.com`
3. Configure o modelo e API Key
4. Inicialize o Oráculo

### Carregar um vídeo do YouTube
1. Selecione "Youtube" como tipo de arquivo
2. Digite a URL do vídeo
3. O Oráculo extrairá a transcrição automaticamente

### Carregar um PDF
1. Selecione "PDF" como tipo de arquivo
2. Faça upload do arquivo PDF
3. O conteúdo será processado e disponibilizado para consultas

## ⚙️ Configuração

O Oráculo suporta os seguintes modelos:

**OpenAI:**
- `gpt-4o-mini`
- `gpt-4o`

**Groq:**
- `llama-3.1-70b-versatile`
- `gemma2-9b-it`
- `mixtral-8x7b-32768`

## 🔒 Segurança

- As API Keys são inseridas como campos de senha (não são exibidas)
- Arquivos temporários são criados durante o processamento e podem ser limpos após o uso


## 🐛 Solução de Problemas

- **Erro ao carregar site:** O Oráculo tenta carregar o site até 5 vezes com User-Agents aleatórios. Se falhar, verifique se a URL está correta e acessível.
- **Conteúdo bloqueado por JavaScript:** O sistema pode sugerir recarregar o Oráculo se o conteúdo parecer bloqueado.
- **Erro de API Key:** Certifique-se de que a API Key está correta e tem créditos/permissões suficientes.

## 📝 Notas

- O Oráculo substitui automaticamente "$" por "s" nas respostas
- O histórico de conversas é mantido durante a sessão
- Cada inicialização do Oráculo limpa o histórico anterior

## 🤝 Contribuindo

Sinta-se à vontade para abrir issues ou pull requests para melhorias!

## 📄 Licença

Este projeto é de uso educacional.

---





