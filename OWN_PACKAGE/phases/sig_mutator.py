import hashlib
import json

from memory_engine import load_memory, save_memory


def mutate_signature(data):
    entropy = hashlib.sha256(json.dumps(data).encode()).hexdigest()
    return entropy[:16]


def rewrite_signatures():
    memory = load_memory()
    for key, entry in memory.items():
        sig = mutate_signature(entry)
        entry["signature"] = sig
        print(f"[+] Signature updated for {key} -> {sig}")
    save_memory(memory)


if __name__ == "__main__":
    rewrite_signatures()
