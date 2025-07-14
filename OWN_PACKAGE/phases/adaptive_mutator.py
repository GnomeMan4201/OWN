import time
import time
import time
import re, os

REDIRECT_LOG = "../logs/adaptive_redirects.log"
OUTPUT_PAYLOADS = "../payloads/adaptive_payloads.txt"

BASE_TEMPLATES = [
    "GET {path} HTTP/1.1\r\nHost: {host}\r\nUser-Agent: BlackICE-Mutator\r\n\r\n",
    "POST {path} HTTP/1.1\r\nHost: {host}\r\nContent-Length: 29\r\n\r\nusername=admin&password=pass123",
]

def extract_redirects():
    wait = 0
    while not os.path.exists(REDIRECT_LOG) and wait < 5:
        time.sleep(1)
        wait += 1
    if not os.path.exists(REDIRECT_LOG):
        print("[!] No redirect log found.")
        os.system("python ../core/adaptive_probe.py")
        return []
    paths = []
    with open(REDIRECT_LOG, "r") as f:
        for line in f:
            match = re.search(r"Location:\s*(http[s]?://[^/]+)(/.*)", line)
            if match:
                host = match.group(1).replace("http://", "").replace("https://", "")
                path = match.group(2)
                paths.append((host, path))
    return paths

def mutate_payloads():
    redirects = extract_redirects()
    if not redirects:
        return

    with open(OUTPUT_PAYLOADS, 'w') as f:
        for host, path in redirects:
            for template in BASE_TEMPLATES:
                payload = template.format(path=path, host=host)
                f.write(payload + '\n')
                print(f"[+] Created adaptive payload for {host}{path}")
    print(f"[*] Saved mutated payloads to {OUTPUT_PAYLOADS}")

if __name__ == "__main__":
    mutate_payloads()
