import socket
from memory_engine import get_top_targets

LOADER = b"#!/bin/sh\necho 'pivot online' > /tmp/pivot_status\n"

def deploy_pivot(ip):
    try:
        s = socket.socket()
        s.connect((ip, 1337))
        s.sendall(LOADER)
        s.close()
        print(f"[+] Pivot loader sent to {ip}:1337")
    except Exception as e:
        print(f"[!] Pivot failed for {ip}:1337 - {e}")

if __name__ == "__main__":
    for t in get_top_targets():
        ip, _ = t.split(":")
        deploy_pivot(ip)
