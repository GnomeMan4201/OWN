import socket
from memory_engine import get_top_targets

def send_syscall_probe(ip, port):
    payload = b"GET /dev/kmem HTTP/1.1\r\nHost: %s\r\n\r\n" % ip.encode()
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, int(port)))
        s.sendall(payload)
        s.recv(1024)
        s.close()
        print(f"[+] Kernel probe sent to {ip}:{port}")
    except Exception as e:
        print(f"[!] Kernel probe failed on {ip}:{port} - {e}")

if __name__ == "__main__":
    for t in get_top_targets():
        ip, port = t.split(":")
        send_syscall_probe(ip, port)
