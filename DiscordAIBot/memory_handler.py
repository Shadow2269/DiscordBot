import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def get_user_memory(user_id: int) -> str:
    memory = load_memory()
    return memory.get(str(user_id), "")

def update_user_memory(user_id: int, new_info: str):
    memory = load_memory()
    user_id_str = str(user_id)
    current = memory.get(user_id_str, "")
    updated = current + "\n" + new_info
    memory[user_id_str] = updated.strip()
    save_memory(memory)
