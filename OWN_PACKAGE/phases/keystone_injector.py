import socket
from memory_engine import get_top_targets

def build_keystone_payload(ip):
    return f"GET /?q=http://{ip}:80/admin HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: KeystoneProbe/1.0\r\n\r\n".encode()

def inject_keystones():
    targets = get_top_targets()
    for t in targets:
        ip, port = t.split(":")
        payload = build_keystone_payload(ip)
        try:
            s = socket.socket()
            s.settimeout(2)
            s.connect((ip, int(port)))
            s.sendall(payload)
            s.close()
            print(f"[+] Keystone injected at {ip}:{port}")
        except Exception as e:
            print(f"[!] Keystone injection failed for {ip}:{port} - {e}")

if __name__ == "__main__":
    inject_keystones()
