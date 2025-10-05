import socket
import threading

from memory_engine import get_top_targets

RESP_TEMPLATE = """HTTP/1.1 200 OK\r
Server: nginx/1.18.0\r
Content-Type: text/html\r
Content-Length: 42\r
\r
<html><body><h1>Admin Portal</h1></body></html>
"""


def handle_client(conn, addr):
    try:
        data = conn.recv(1024)
        if data:
            conn.sendall(RESP_TEMPLATE.encode())
    finally:
        conn.close()


def start_phantom(ip="0.0.0.0", port=8081):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    s.listen(5)
    print(f"[*] Phantom mirror online at {ip}:{port}")
    while True:
        client, addr = s.accept()
        threading.Thread(target=handle_client, args=(client, addr)).start()


if __name__ == "__main__":
    start_phantom()
