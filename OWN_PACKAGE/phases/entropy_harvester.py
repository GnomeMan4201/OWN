import socket, ssl
from memory_engine import get_top_targets

def fingerprint_tls(ip, port):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=ip) as s:
            s.settimeout(3)
            s.connect((ip, int(port)))
            cert = s.getpeercert()
            sig_algos = cert.get('signatureAlgorithm', 'unknown')
            print(f"[+] TLS fingerprint {ip}:{port} => {sig_algos}")
    except Exception as e:
        print(f"[!] Fingerprint fail {ip}:{port} - {e}")

if __name__ == "__main__":
    for t in get_top_targets():
        ip, port = t.split(":")
        fingerprint_tls(ip, port)
