import socket, time
from memory_engine import get_top_targets

def ping_host(ip, port):
    payload = f"HEAD / HTTP/1.1\r\nHost: {ip}\r\n\r\n".encode()
    try:
        s = socket.socket()
        s.settimeout(5)
        start = time.time()
        s.connect((ip, int(port)))
        s.sendall(payload)
        s.recv(1024)
        end = time.time()
        s.close()
        return round(end - start, 4)
    except:
        return -1

def analyze_drift(samples=3):
    targets = get_top_targets()
    print(f"[*] Probing {len(targets)} targets for latency drift...")
    for t in targets:
        ip, port = t.split(":")
        times = [ping_host(ip, port) for _ in range(samples)]
        if -1 in times:
            continue
        avg = sum(times) / len(times)
        delta = max(times) - min(times)
        print(f"[+] {ip}:{port} - Avg: {avg:.3f}s | Drift: {delta:.3f}s")

if __name__ == "__main__":
    analyze_drift()
