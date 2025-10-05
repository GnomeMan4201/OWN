import random
import socket

from memory_engine import get_top_targets

DEVICE_HEADERS = [
    ("Android", "Dalvik/2.1.0 (Linux; U; Android 10)"),
    ("iPhone", "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)"),
    ("Windows", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"),
    ("Linux", "Mozilla/5.0 (X11; Linux x86_64)"),
]


def mimic(ip, port):
    ua = random.choice(DEVICE_HEADERS)[1]
    payload = f"GET /status HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {ua}\r\n\r\n".encode()
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, int(port)))
        s.sendall(payload)
        s.close()
        print(f"[+] Fingerprint mimic [{ua}] sent to {ip}:{port}")
    except Exception as e:
        print(f"[!] Failed to mimic {ip}:{port} - {e}")


if __name__ == "__main__":
    for t in get_top_targets():
        ip, port = t.split(":")
        mimic(ip, port)
