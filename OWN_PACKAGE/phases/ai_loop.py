import os
from memory_engine import log_interaction
import dpkt, socket, json, time, subprocess
from pathlib import Path

PROFILES_FILE = "../core/behavior_profiles.json"
CAPTURE_FILE = "../logs/capture.pcap"

def load_profiles():
    try:
        with open(PROFILES_FILE) as f:
            return json.load(f)
    except:
        return {}

def match_triggers(payload, triggers):
    text = payload.decode('utf-8', errors='ignore')
    matched = []
    for keyword in triggers:
        if keyword in text:
            matched.append(keyword)
    return matched

def take_action(actions, payload, dst_ip, dport):
    for action in actions:
        if action == "alert":
            print(f"[!] ALERT: {payload[:100]!r}")
        elif action == "inject":
            print(f"[*] Injecting payload into {dst_ip}:{dport}")
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((dst_ip, dport))
                s.sendall(payload)
                resp = s.recv(1024)

                if b"403" in resp:

                    memory[key]["score"] -= 2

                elif b"200" in resp and b"Set-Cookie" in resp:

                    memory[key]["score"] += 3
                log_interaction(dst_ip, dport, payload, "success")
                s.close()
                print("[+] Injected successfully.")
            except Exception as e:
                log_interaction(dst_ip, dport, payload, "fail")
                print(f"[!] Injection failed: {e}")
        elif action == "spoof":
            subprocess.Popen(["python", "../modules/dns_spoof.py"])
        elif action == "replay":
            subprocess.Popen(["python", "../replays/replay_attack.py"])

def monitor():
    profiles = load_profiles()
    print("[*] BlackICE AI loop engaged.")
    if not Path(CAPTURE_FILE).exists():
        print(f"[!] No pcap at {CAPTURE_FILE}")
        return

    with open(CAPTURE_FILE, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        for ts, buf in pcap:
            try:
                eth = dpkt.ethernet.Ethernet(buf)
                if not isinstance(eth.data, dpkt.ip.IP): continue
                ip = eth.data
                if not isinstance(ip.data, dpkt.tcp.TCP): continue
                tcp = ip.data
                if not tcp.data: continue

                payload = tcp.data
                dst_ip = socket.inet_ntoa(ip.dst)
                dport = tcp.dport

                for profile in profiles:
                    matched = match_triggers(payload, profiles[profile]["triggers"])
                    if matched:
                        print(f"[AI] Matched {profile} profile: {matched}")
                        take_action(profiles[profile]["actions"], payload, dst_ip, dport)
            except Exception as e:
                log_interaction(dst_ip, dport, payload, "fail")
                continue
    os.system("python ../core/adaptive_mutator.py")
    from memory_engine import log_interaction
    print("[*] AI loop completed.")

def monitor():
    profiles = load_profiles()
    print("[*] BlackICE AI loop engaged.")
    if not Path(CAPTURE_FILE).exists():
        print(f"[!] No pcap at {CAPTURE_FILE}")
        return

    with open(CAPTURE_FILE, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        for ts, buf in pcap:
            try:
                eth = dpkt.ethernet.Ethernet(buf)
                if not isinstance(eth.data, dpkt.ip.IP): continue
                ip = eth.data
                if not isinstance(ip.data, dpkt.tcp.TCP): continue
                tcp = ip.data
                if not tcp.data: continue

                payload = tcp.data
                dst_ip = socket.inet_ntoa(ip.dst)
                dport = tcp.dport

                for profile in profiles:
                    matched = match_triggers(payload, profiles[profile]["triggers"])
                    if matched:
                        print(f"[AI] Matched {profile} profile: {matched}")
                        take_action(profiles[profile]["actions"], payload, dst_ip, dport)
            except Exception as e:
                log_interaction(dst_ip, dport, payload, "fail")
                continue
    os.system("python ../core/adaptive_mutator.py")
    from memory_engine import log_interaction
    print("[*] AI loop completed.")

if __name__ == "__main__":
    monitor()
