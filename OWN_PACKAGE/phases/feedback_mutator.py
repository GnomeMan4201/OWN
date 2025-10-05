import json
import os
import re
from urllib.parse import urlparse

from memory_engine import load_memory

REDIRECTS = []


def extract_redirect_domains():
    memory = load_memory()
    for v in memory.values():
        for i in v["interactions"]:
            match = re.search(r"Location: (http[^\r\n]+)", i["result"])
            if match:
                domain = urlparse(match.group(1)).netloc
                REDIRECTS.append(domain)


def adaptive_fuzz():
    extract_redirect_domains()
    fuzzed = []
    for d in REDIRECTS:
        fuzzed.append(f"GET /admin HTTP/1.1\r\nHost: {d}\r\n\r\n")
        fuzzed.append(
            f"POST /login HTTP/1.1\r\nHost: {d}\r\n\r\nusername=admin&password=<script>"
        )
    return fuzzed


if __name__ == "__main__":
    for payload in adaptive_fuzz():
        print(f"[+] Generated redirect-tuned payload:\n{payload}")
