import os
import speech_recognition as sr
from gtts import gTTS

def hablar(texto):
    """Convierte texto en voz usando gTTS."""
    tts = gTTS(text=texto, lang="es")
    tts.save("respuesta.mp3")
    os.system("mpg123 respuesta.mp3")  # En Linux (requiere mpg123)
    os.remove("respuesta.mp3")

def escuchar_comando():
    """Escucha al usuario y devuelve el texto reconocido."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Escuchando...")
        audio = r.listen(source)

    try:
        comando = r.recognize_google(audio, language="es-ES")
        print(f"👉 Entendí: {comando}")
        return comando.lower()
    except:
        return ""
