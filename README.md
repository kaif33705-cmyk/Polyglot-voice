# 🌍 Polyglot Voice Translator 🎙

An AI-powered multi-language translator that supports both *text input* and *voice-based translation, with **audio output* using gTTS. Built using Python, Streamlit, Google Translate API, and Speech Recognition.

---

## 🚀 Features

- 🔠 *Text Translation* between 15+ languages
- 🎤 *Speech-to-Text Translation* using your microphone
- 🔊 *Audio Output* for translated text
- 🌐 Powered by [deep-translator](https://pypi.org/project/deep-translator/) and [gTTS](https://pypi.org/project/gTTS/)
- 🧠 Streamlit UI for smooth user interaction

---

## 📸 Demo Preview

![App Screenshot](https://via.placeholder.com/800x400.png?text=Polyglot+Voice+Demo)

---

## 🛠 Tech Stack

- *Frontend*: Streamlit
- *Translation*: Deep Translator (Google Translate API)
- *Voice Input*: SpeechRecognition
- *Text-to-Speech*: gTTS
- *Backend*: Python

---

## 🌐 Supported Languages

| Name              | Code   |
|-------------------|--------|
| English           | en     |
| Hindi             | hi     |
| Spanish           | es     |
| French            | fr     |
| Arabic            | ar     |
| Bengali           | bn     |
| Russian           | ru     |
| Portuguese        | pt     |
| Urdu              | ur     |
| Indonesian        | id     |
| German            | de     |
| Japanese          | ja     |
| Turkish           | tr     |
| Vietnamese        | vi     |
| Chinese (Simplified) | zh-CN |

---

## 💻 How to Run Locally

```bash
git clone https://github.com/kaif33705-cmyk/Polyglot-voice.git
cd Polyglot-voice
pip install -r requirements.txt
streamlit run app.py