import random

from memory_engine import get_top_targets

FAKE_OSINT = {
    "93.184.216.34": "Comcast Gateway - Model TG1682G - Known exploit CVE-2023-4567",
}


def enrich():
    for t in get_top_targets():
        ip = t.split(":")[0]
        info = FAKE_OSINT.get(ip, "No OSINT match.")
        print(f"[+] OSINT for {ip}: {info}")


if __name__ == "__main__":
    enrich()
