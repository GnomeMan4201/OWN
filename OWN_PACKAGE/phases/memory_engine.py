import json, os
from datetime import datetime

MEMORY_FILE = "../sessions/target_memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, 'r') as f:
        return json.load(f)

def save_memory(data):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def log_interaction(ip, port, payload, result):
    memory = load_memory()
    key = f"{ip}:{port}"
    timestamp = datetime.utcnow().isoformat()

    if key not in memory:
        memory[key] = {
            "interactions": [],
            "score": 0
        }

    memory[key]["interactions"].append({
        "time": timestamp,
        "payload": payload.decode(errors="ignore"),
        "result": result
    })

    # Basic scoring model
    if result == "success":
        memory[key]["score"] += 1
    elif result == "fail":
        memory[key]["score"] -= 1

    save_memory(memory)

def get_top_targets(threshold=1):
    memory = load_memory()
    return [k for k, v in memory.items() if v.get("score", 0) >= threshold]


def get_top_targets(threshold=1):
    memory = load_memory()
    return [k for k, v in memory.items() if v.get("score", 0) >= threshold]
