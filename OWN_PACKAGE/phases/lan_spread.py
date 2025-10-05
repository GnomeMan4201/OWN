import os
import socket

from memory_engine import load_memory, save_memory


def get_local_subnet():
    ip = socket.gethostbyname(socket.gethostname())
    base = ".".join(ip.split(".")[:3]) + "."
    return [base + str(i) for i in range(1, 255)]


def expand_targets():
    memory = load_memory()
    for ip in get_local_subnet():
        key = f"{ip}:80"
        if key not in memory:
            memory[key] = {"interactions": [], "score": 0}
    save_memory(memory)
    print(f"[+] Subnet targets loaded into memory.")


if __name__ == "__main__":
    expand_targets()
