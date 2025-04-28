import json
import os

MEMORY_FILE = "memory.json"

# Sicherstellen, dass die Datei existiert
if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump({}, f)

def load_memory():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

def add_message(user_id, message):
    memory = load_memory()
    user_id = str(user_id)
    
    if user_id not in memory:
        memory[user_id] = []

    memory[user_id].append(message)
    
    # Optional: Limit auf z.B. die letzten 50 Nachrichten
    memory[user_id] = memory[user_id][-50:]

    save_memory(memory)

def get_user_history(user_id):
    memory = load_memory()
    return memory.get(str(user_id), [])
