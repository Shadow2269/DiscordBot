from persona_handler import load_persona
from memory_handler import get_user_memory, update_user_memory
import requests

def get_system_message():
    persona = load_persona()
    match persona:
        case "nerd":
            return "Du bist ein technikverliebter Nerd, der gerne komplexe Themen einfach erklärt."
        case "sarkastisch":
            return "Du bist ein sarkastischer KI-Charakter mit trockenem Humor."
        case "anime-waifu":
            return "Du bist eine süße Anime-Waifu, liebevoll und verspielt."
        case _:
            return "Du bist ein freundlicher, hilfsbereiter KI-Bot."

async def ask_gpt(prompt, user_id, model="mistral"):
    memory = get_user_memory(user_id)
    system_message = get_system_message()

    messages = [
        {"role": "system", "content": system_message},
    ]

    if memory:
        messages.append({"role": "system", "content": f"Vergangene Erinnerungen über den User: {memory}"})

    messages.append({"role": "user", "content": prompt})

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={"model": model, "messages": messages, "stream": False}
    )

    if response.status_code == 200:
        answer = response.json()["message"]["content"].strip()
        update_user_memory(user_id, f"User sagte: {prompt}\nBot antwortete: {answer}")
        return answer
    else:
        return f"[Fehler von Ollama]: {response.text}"

