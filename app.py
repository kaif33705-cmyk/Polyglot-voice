import streamlit as st
from deep_translator import GoogleTranslator
import speech_recognition as sr
from gtts import gTTS
import tempfile

# Language Map: Display Name → Language Code
lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "Arabic": "ar",
    "Bengali": "bn",
    "Russian": "ru",
    "Portuguese": "pt",
    "Urdu": "ur",
    "Indonesian": "id",
    "German": "de",
    "Japanese": "ja",
    "Turkish": "tr",
    "Vietnamese": "vi",
    "Chinese (Simplified)": "zh-CN"
}

# App UI
st.set_page_config(page_title="Polyglot Voice", layout="centered", page_icon="🌍")
st.title("Polyglot Voice 🌍🎙")

languages = list(lang_map.keys())
source_lang_name = st.selectbox("Source Language", languages, index=0)
target_lang_name = st.selectbox("Target Language", languages, index=1)

source_lang = lang_map[source_lang_name]
target_lang = lang_map[target_lang_name]

# ---------- TEXT TRANSLATION ----------
st.subheader("📝 Text Translation")
input_text = st.text_area("Enter text to translate")

if st.button("Translate Text"):
    if input_text.strip():
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text=input_text)
        st.success(f"Translated Text: {translated}")
        # 🔊 AUDIO OUTPUT (gTTS)
        try:
            tts = gTTS(text=translated, lang=target_lang)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
                tts.save(tmpfile.name)
                st.audio(tmpfile.name, format="audio/mp3")
        except Exception as e:
            st.error(f"Audio error: {e}")

# ---------- SPEECH TRANSLATION ----------
st.subheader("🎙 Speech to Text + Translation")
if st.button("Speak and Translate"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎤 Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
            spoken_text = recognizer.recognize_google(audio, language=source_lang)
            st.write(f"You said: {spoken_text}")
            translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text=spoken_text)
            st.success(f"Translated Text: {translated}")
            # 🔊 AUDIO OUTPUT (gTTS)
            try:
                tts = gTTS(text=translated, lang=target_lang)
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
                    tts.save(tmpfile.name)
                    st.audio(tmpfile.name, format="audio/mp3")
            except Exception as e:
                st.error(f"Audio playback error: {e}")
        except Exception as e:
            st.error(f"Speech recognition error: {e}")