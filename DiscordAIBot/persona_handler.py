import json
import os

FILE = "persona.json"

def save_persona(style):
    with open(FILE, "w") as f:
        json.dump({"persona": style}, f)

def load_persona():
    if not os.path.exists(FILE):
        return "normal"
    with open(FILE, "r") as f:
        return json.load(f).get("persona", "normal")
