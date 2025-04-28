import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")

# Dein HuggingFace Modell
MODEL = "google/flan-t5-small"  # Einfaches Modell (du kannst es später upgraden)

# Persönlichkeit des Bots
system_prompt = (
    "Du bist Razey, ein freundlicher und frecher Discord-Chatbot. "
    "Antworte locker, benutze Emojis, und sei hilfreich."
)

# Speicherdatei
memory_file = "memory.json"

# Lade alte Konversationen
def load_memory():
    try:
        with open(memory_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_message(message):
    memory = load_memory()
    memory.append(message)
    with open(memory_file, "w") as f:
        json.dump(memory[-20:], f, indent=2)  # Maximal die letzten 20 Nachrichten speichern

# Anfrage an HuggingFace
def get_bot_response(user_message):
    history = load_memory()
    prompt = system_prompt + "\n" + "\n".join(history) + f"\nUser: {user_message}\nBot:"

    response = requests.post(
        f"https://api-inference.huggingface.co/models/{MODEL}",
        headers={"Authorization": f"Bearer {HF_API_KEY}"},
        json={"inputs": prompt}
    )

    if response.status_code != 200:
        return "❌ Fehler bei der Anfrage."

    generated_text = response.json()
    try:
        output = generated_text[0]["generated_text"].split("Bot:")[-1].strip()
        return output
    except (KeyError, IndexError):
        return "❌ Konnte keine Antwort generieren."

