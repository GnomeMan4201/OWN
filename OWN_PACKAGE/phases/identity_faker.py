import random
import socket

from memory_engine import get_top_targets

FAKE_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0",
    "curl/7.68.0",
    "python-requests/2.28.1",
    "PostmanRuntime/7.32.2",
    "Go-http-client/2.0",
]


def embed_identity(ip, port):
    ua = random.choice(FAKE_AGENTS)
    payload = f"GET /login HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {ua}\r\n\r\n".encode()
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, int(port)))
        s.sendall(payload)
        s.close()
        print(f"[+] Synthetic ID [{ua}] propagated to {ip}:{port}")
    except Exception as e:
        print(f"[!] Failed to send identity to {ip}:{port} - {e}")


def deploy_identities():
    for t in get_top_targets():
        ip, port = t.split(":")
        embed_identity(ip, port)


if __name__ == "__main__":
    deploy_identities()
