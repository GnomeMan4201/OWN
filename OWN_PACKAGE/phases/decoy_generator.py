import os, socket, threading, random
from memory_engine import get_top_targets

DECoy_HTML = """<html><head><title>Login Portal</title></head><body>
<h2>Device Update Required</h2>
<form><input type='text' name='user' /><input type='password' name='pass' /><input type='submit' value='Login'></form>
</body></html>"""

def serve_decoy(ip="0.0.0.0", port=8888):
    def handle(client, addr):
        try:
            client.recv(1024)
            client.sendall(f"""HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {len(DECoy_HTML)}\r\n\r\n{DECoy_HTML}""".encode())
        finally:
            client.close()

    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    s.listen(5)
    print(f"[+] Decoy web service running on port {port}")
    while True:
        client, addr = s.accept()
        threading.Thread(target=handle, args=(client, addr)).start()

if __name__ == "__main__":
    serve_decoy()
