import socket
import time

from memory_engine import get_top_targets


def probe(ip, port):
    payload = "GET /honeypot_probe HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip).encode()
    try:
        s = socket.socket()
        s.settimeout(1.5)
        start = time.time()
        s.connect((ip, int(port)))
        s.sendall(payload)
        banner = s.recv(64)
        latency = time.time() - start
        s.close()
        if b"Honey" in banner or latency < 0.1:
            print(f"[!] Honeynet suspected: {ip}:{port}")
        else:
            print(f"[+] Legit target: {ip}:{port}")
    except:
        pass


if __name__ == "__main__":
    for t in get_top_targets():
        ip, port = t.split(":")
        probe(ip, port)
