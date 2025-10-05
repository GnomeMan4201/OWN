import hashlib
import json
import os
import random

from memory_engine import load_memory

OUTPUT = "../payloads/neural_payloads.txt"


def mutate(payload):
    base = payload.replace("admin", random.choice(["root", "sys", "manager"]))
    fuzz = random.choice(["%00", "'", '"', "<script>", " OR 1=1 -- "])
    if "password" in base:
        base = base.replace("password", "password" + fuzz)
    return base


def hash_payload(p):
    return hashlib.md5(p.encode()).hexdigest()


def run():
    memory = load_memory()
    generated = set()
    with open(OUTPUT, "w") as f:
        for k, v in memory.items():
            for i in v["interactions"]:
                if i["result"] != "success":
                    continue
                p = i["payload"]
                m = mutate(p)
                h = hash_payload(m)
                if h not in generated:
                    f.write(m + "\n")
                    generated.add(h)
                    print(f"[+] Neural payload generated for {k}")


if __name__ == "__main__":
    run()
