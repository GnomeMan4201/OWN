import socket

from memory_engine import get_top_targets


def escalate():
    targets = get_top_targets()
    if not targets:
        print("[!] No high-priority targets in memory.")
        return

    print(f"[*] Escalating to {len(targets)} top targets.")
    for entry in targets:
        ip, port = entry.split(":")
        port = int(port)
        payload = f"GET /admin HTTP/1.1\r\nHost: {ip}\r\n\r\n".encode()
        try:
            s = socket.socket()
            s.settimeout(2)
            s.connect((ip, port))
            s.sendall(payload)
            s.close()
            print(f"[+] Escalation probe sent to {ip}:{port}")
        except Exception as e:
            print(f"[!] Escalation failed for {ip}:{port} - {e}")


if __name__ == "__main__":
    escalate()
