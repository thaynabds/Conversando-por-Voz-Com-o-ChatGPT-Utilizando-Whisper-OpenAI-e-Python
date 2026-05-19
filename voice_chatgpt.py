"""
🎙️ Voice ChatGPT com Whisper + gTTS
Desafio de Projeto DIO — Speech-to-Text & Text-to-Speech
Autora: Thayná Batista da Silva
Curso: Análise e Desenvolvimento de Sistemas — Faculdade Senac Recife-PE
"""

import os
import openai
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import tempfile


# ──────────────────────────────────────────────
# CONFIGURAÇÃO
# ──────────────────────────────────────────────

openai.api_key = os.getenv("OPENAI_API_KEY")  # Configure sua chave no ambiente

IDIOMA_ENTRADA  = "pt-BR"   # Idioma para reconhecimento de voz
IDIOMA_RESPOSTA = "pt"      # Idioma para síntese de voz (gTTS)
MODELO_GPT      = "gpt-3.5-turbo"
MODELO_WHISPER  = "whisper-1"


# ──────────────────────────────────────────────
# FUNÇÕES PRINCIPAIS
# ──────────────────────────────────────────────

def gravar_audio(duracao: int = 5) -> bytes:
    """Grava áudio do microfone e retorna os bytes de WAV."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"\n🎤 Fale agora... (até {duracao}s)")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=duracao, phrase_time_limit=duracao)
    return audio.get_wav_data()


def transcrever_audio(audio_bytes: bytes) -> str:
    """Transcreve áudio usando o modelo Whisper da OpenAI."""
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    try:
        with open(tmp_path, "rb") as f:
            resposta = openai.Audio.transcribe(
                model=MODELO_WHISPER,
                file=f,
                language=IDIOMA_ENTRADA.split("-")[0],
            )
        texto = resposta["text"].strip()
        print(f"📝 Você disse: {texto}")
        return texto
    finally:
        os.remove(tmp_path)


def perguntar_ao_chatgpt(pergunta: str, historico: list) -> str:
    """Envia a pergunta ao ChatGPT e retorna a resposta em texto."""
    historico.append({"role": "user", "content": pergunta})

    resposta = openai.ChatCompletion.create(
        model=MODELO_GPT,
        messages=[
            {
                "role": "system",
                "content": (
                    "Você é um assistente prestativo e amigável. "
                    "Responda de forma clara e concisa em português."
                ),
            },
            *historico,
        ],
    )

    texto_resposta = resposta["choices"][0]["message"]["content"].strip()
    historico.append({"role": "assistant", "content": texto_resposta})
    print(f"🤖 ChatGPT: {texto_resposta}\n")
    return texto_resposta


def falar_resposta(texto: str) -> None:
    """Converte texto em fala usando gTTS e reproduz o áudio."""
    tts = gTTS(text=texto, lang=IDIOMA_RESPOSTA, slow=False)
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
        tts.save(tmp.name)
        tmp_path = tmp.name

    try:
        playsound(tmp_path)
    finally:
        os.remove(tmp_path)


# ──────────────────────────────────────────────
# LOOP PRINCIPAL
# ──────────────────────────────────────────────

def main() -> None:
    print("=" * 55)
    print("  🎙️  Voice ChatGPT — Whisper + gTTS + OpenAI")
    print("  Autora: Thayná Batista da Silva — Senac Recife")
    print("=" * 55)
    print("Diga 'sair' ou 'encerrar' para terminar.\n")

    historico: list = []

    while True:
        try:
            audio = gravar_audio(duracao=7)
            texto = transcrever_audio(audio)

            if not texto:
                print("⚠️  Não consegui entender. Tente novamente.\n")
                continue

            if any(cmd in texto.lower() for cmd in ["sair", "encerrar", "exit", "quit"]):
                print("👋 Encerrando. Até a próxima!")
                falar_resposta("Encerrando. Até a próxima!")
                break

            resposta = perguntar_ao_chatgpt(texto, historico)
            falar_resposta(resposta)

        except KeyboardInterrupt:
            print("\n👋 Interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"❌ Erro: {e}\n")


if __name__ == "__main__":
    main()
