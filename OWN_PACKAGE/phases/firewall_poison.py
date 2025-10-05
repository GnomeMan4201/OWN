import random
import socket
import time

from memory_engine import get_top_targets


def generate_noise(ip, port):
    fake_paths = ["/login", "/update", "/status", "/info", "/health"]
    for _ in range(random.randint(3, 7)):
        path = random.choice(fake_paths)
        req = f"GET {path} HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: LegitMonitor/2.0\r\n\r\n".encode()
        try:
            s = socket.socket()
            s.settimeout(1.5)
            s.connect((ip, int(port)))
            s.sendall(req)
            s.close()
            print(f"[+] Noise sent to {ip}:{path}")
            time.sleep(0.4)
        except:
            pass


if __name__ == "__main__":
    for tgt in get_top_targets():
        ip, port = tgt.split(":")
        generate_noise(ip, port)
