import base64, random
from memory_engine import get_top_targets

BASE_PAYLOAD = "GET /login HTTP/1.1\r\nHost: {host}\r\nUser-Agent: BlackICE\r\n\r\n"

def mutate_payload(payload):
    junk = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=random.randint(3, 7)))
    encoded = base64.b64encode(payload.encode()).decode()
    return f"{junk}:{encoded}"

def deploy_mutations():
    for t in get_top_targets():
        ip, port = t.split(":")
        mutated = mutate_payload(BASE_PAYLOAD.format(host=ip))
        print(f"[+] Polymorphed payload for {ip}:{port}:")
        print(mutated)

if __name__ == "__main__":
    deploy_mutations()
