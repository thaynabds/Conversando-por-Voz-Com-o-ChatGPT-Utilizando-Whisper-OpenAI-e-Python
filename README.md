# Conversando-por-Voz-Com-o-ChatGPT-Utilizando-Whisper-OpenAI-e-Python
---
<div align="center">

# 🎙️ Voice ChatGPT
### Conversando por Voz com o ChatGPT usando Whisper (OpenAI) e Python

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-Whisper%20%2B%20GPT-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![gTTS](https://img.shields.io/badge/gTTS-Text--to--Speech-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://pypi.org/project/gTTS/)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-Notebook-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com/)
[![DIO](https://img.shields.io/badge/DIO-Desafio%20de%20Projeto-E91E63?style=for-the-badge&logo=dio&logoColor=white)](https://dio.me/)

<br/>

> Projeto desenvolvido como parte do Desafio de Projeto da **DIO (Digital Innovation One)** —  
> unindo **Speech-to-Text**, **Inteligência Artificial** e **Text-to-Speech** em uma solução de voz multi-idiomas.

</div>

---

## 📌 Sobre o Projeto

Este projeto implementa um assistente de voz inteligente que combina três tecnologias poderosas da IA moderna:

| Tecnologia | Função |
|---|---|
| 🎤 **Whisper (OpenAI)** | Converte sua fala em texto (*Speech-to-Text*) com suporte a múltiplos idiomas |
| 🤖 **ChatGPT (OpenAI)** | Processa a pergunta e gera uma resposta inteligente via API |
| 🔊 **gTTS (Google)** | Converte a resposta em fala (*Text-to-Speech*) de forma natural |

O fluxo completo permite **conversar com o ChatGPT usando apenas a voz**, recebendo respostas também por áudio — criando uma experiência de diálogo verdadeiramente imersiva.

---

## 🏗️ Arquitetura da Solução

```
  🎤 Microfone
      │
      ▼
  Captura de Áudio (SpeechRecognition / JavaScript)
      │
      ▼
  ┌─────────────────────────┐
  │  Whisper API (OpenAI)   │  ◄── Speech-to-Text
  │  Transcrição do áudio   │
  └─────────────┬───────────┘
                │  texto transcrito
                ▼
  ┌─────────────────────────┐
  │  ChatGPT API (OpenAI)   │  ◄── Processamento NLP
  │  gpt-3.5-turbo          │
  └─────────────┬───────────┘
                │  resposta em texto
                ▼
  ┌─────────────────────────┐
  │  gTTS (Google)          │  ◄── Text-to-Speech
  │  Síntese de voz         │
  └─────────────┬───────────┘
                │
                ▼
            🔊 Resposta em áudio
```

---

## 📁 Estrutura do Repositório

```
voice-chatgpt/
│
├── 📓 voice_chatgpt_colab.ipynb   # Notebook completo para Google Colab
├── 🐍 voice_chatgpt.py            # Script para execução local
├── 📋 requirements.txt            # Dependências do projeto
├── 🔒 .env.example                # Exemplo de variáveis de ambiente
├── 🚫 .gitignore                  # Arquivos ignorados pelo Git
└── 📖 README.md                   # Documentação do projeto
```

---

## 🚀 Como Executar

### ☁️ Opção 1 — Google Colab (Recomendado)

1. Acesse o notebook: **[`voice_chatgpt_colab.ipynb`](./voice_chatgpt_colab.ipynb)**
2. Faça upload para o [Google Colab](https://colab.research.google.com/) ou use o link oficial do curso
3. Insira sua `OPENAI_API_KEY` na célula de configuração
4. Execute as células em ordem e clique em **"Permitir microfone"** quando solicitado
5. Fale quando a célula de gravação estiver ativa 🎤

> 💡 **Link do Colab original do curso:** [bit.ly/41XfKaM](https://bit.ly/41XfKaM)

---

### 💻 Opção 2 — Execução Local

**Pré-requisitos:** Python 3.9+, pip, microfone ativo

```bash
# 1. Clone o repositório
git clone https://github.com/thaynabds/voice-chatgpt.git
cd voice-chatgpt

# 2. Crie e ative um ambiente virtual (opcional, mas recomendado)
python -m venv .venv
source .venv/bin/activate       # Linux/macOS
.venv\Scripts\activate          # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure sua chave de API
cp .env.example .env
# Edite o arquivo .env e adicione sua OPENAI_API_KEY

# 5. Execute
python voice_chatgpt.py
```

---

## 🔑 Configurando a API Key

1. Acesse [platform.openai.com](https://platform.openai.com/)
2. Vá em **API Keys → Create new secret key**
3. Copie a chave e adicione ao arquivo `.env`:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> ⚠️ **Nunca compartilhe sua API Key nem faça commit do arquivo `.env`!**

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3.9+](https://www.python.org/)** — Linguagem principal
- **[OpenAI Whisper](https://openai.com/research/whisper)** — Transcrição de áudio (Speech-to-Text)
- **[OpenAI ChatGPT](https://platform.openai.com/docs/)** — Modelo de linguagem `gpt-3.5-turbo`
- **[gTTS](https://pypi.org/project/gTTS/)** — Google Text-to-Speech para síntese de voz
- **[SpeechRecognition](https://pypi.org/project/SpeechRecognition/)** — Captura de áudio local
- **[Google Colab](https://colab.research.google.com/)** — Ambiente de execução em nuvem

---

## 📚 Referências e Recursos

| Recurso | Link |
|---|---|
| 📄 Artigo completo do projeto | [Conversando Por Voz Com o ChatGPT](https://web.dio.me/articles/conversando-por-voz-com-o-chatgpt-utilizando-whisper-openai-e-python) |
| 📓 Notebook no Google Colab | [bit.ly/41XfKaM](https://bit.ly/41XfKaM) |
| 🎥 Live no YouTube da DIO | [bit.ly/44e9Nrw](https://bit.ly/44e9Nrw) |
| 🌐 Plataforma DIO | [dio.me](https://dio.me/) |
| 📖 Documentação OpenAI | [platform.openai.com/docs](https://platform.openai.com/docs/) |
| 📖 Documentação gTTS | [gtts.readthedocs.io](https://gtts.readthedocs.io/) |

---

## 👩‍💻 Autora

<div align="center">

**Thayná Batista da Silva**  
Aluna de Análise e Desenvolvimento de Sistemas  
Faculdade Senac Recife-PE · Turma 2025 · Formação prevista: 2027

</div>

---

## 📬 Contato

<div align="center">
  <a href="https://br.linkedin.com/in/thaynabds" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://www.instagram.com/thaynabdstec/" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" />
  </a>
</div>

📧 Email: [thaynabdstec@gmail.com](mailto:thaynabdstec@gmail.com)  
📱 Telefone: +55 (81) 97912-6121

<div align="center">

![Cartão TEC Thayná](https://raw.githubusercontent.com/thaynabds/AppMedSmart/refs/heads/main/Cart%C3%A3o%20TEC%20Thayn%C3%A1%20Batista%20da%20Silva.png)

</div>

---

<div align="center">

Feito com 💜 por **Thayná Batista da Silva** durante o Bootcamp da **DIO**

</div>
