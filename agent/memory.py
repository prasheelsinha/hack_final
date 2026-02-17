import json
from config import MEMORY_FILE

def load_memory():
    try:
        return json.load(open(MEMORY_FILE))
    except:
        return []

def save_memory(entry):
    mem = load_memory()
    mem.append(entry)
    json.dump(mem, open(MEMORY_FILE, "w"), indent=2)