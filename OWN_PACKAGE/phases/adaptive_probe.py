import socket
import ssl
import time

COMMON_PORTS = [80, 443, 8080, 8443]
PROBE_PAYLOAD = b"GET / HTTP/1.1\r\nHost: {}\r\nUser-Agent: BlackICE-AI\r\nConnection: close\r\n\r\n"

def probe_host(ip, ports=COMMON_PORTS, timeout=2):
    print(f"[*] Probing host: {ip}")
    for port in ports:
        try:
            print(f"[>] Connecting to {ip}:{port}...")
            s = socket.socket()
            s.settimeout(timeout)
            s.connect((ip, port))

            if port in [443, 8443]:
                context = ssl.create_default_context()
                s = context.wrap_socket(s, server_hostname=ip)

            payload = PROBE_PAYLOAD.decode().format(ip).encode()
            s.sendall(payload)
            response = b''
            while True:
                data = s.recv(4096)
                if not data:
                    break
                response += data
            s.close()

            headers = response.decode(errors='ignore').split("\r\n\r\n")[0]
            print(f"[+] {ip}:{port} Response:\n{headers}\n")

            if "Apache" in headers or "nginx" in headers or "IIS" in headers:
                print(f"[AI] Detected Web Server Signature: {port} -> {headers.splitlines()[0]}")

            if "Set-Cookie" in headers:
                print(f"[AI] Set-Cookie header found -> Potential Session Handler")

        except Exception as e:
            print(f"[!] Failed {ip}:{port} - {e}")

if __name__ == "__main__":
    target_ip = "93.184.216.34"  # Example (test.com)
    probe_host(target_ip)
