import socket

def dns_reverse(ip):
    try:
        name = socket.gethostbyaddr(ip)[0]
        print(f"[+] Hostname for {ip}: {name}")
        return name
    except:
        return None

def scan(targets):
    for t in targets:
        ip, _ = t.split(":")
        dns_reverse(ip)

if __name__ == "__main__":
    from memory_engine import get_top_targets
    scan(get_top_targets())
