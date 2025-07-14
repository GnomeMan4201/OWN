import os, time, subprocess

LOG_DIR = "../logs"
SEEN = set()

def watch_logs():
    print("[*] Watching logs for new PCAPs...")
    while True:
        files = [f for f in os.listdir(LOG_DIR) if f.endswith('.pcap')]
        for f in files:
            full_path = os.path.join(LOG_DIR, f)
            if full_path not in SEEN:
                SEEN.add(full_path)
                print(f"[+] Detected: {f}")
                subprocess.call(["python", "pcap_parser.py"])
        time.sleep(3)

if __name__ == "__main__":
    watch_logs()
