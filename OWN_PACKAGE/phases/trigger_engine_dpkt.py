import argparse
import json
import socket

import dpkt

TRIGGER_PROFILES = {
    "auth": {
        "admin": "ALERT: Admin access detected",
        "password": "ALERT: Password in transit",
        "Authorization": "ALERT: Auth header found",
        "login": "ALERT: Login form used",
    },
    "tokens": {"token=": "ALERT: Token leak", "sessionid=": "ALERT: Session ID leak"},
    "finance": {
        "creditcard": "ALERT: Credit card data found",
        "iban": "ALERT: IBAN info leak",
        "paypal": "ALERT: PayPal activity",
    },
    "all": {},  # fallback to all keywords
}


def build_trigger_set(profile):
    if profile in TRIGGER_PROFILES and profile != "all":
        return TRIGGER_PROFILES[profile]
    all_triggers = {}
    for d in TRIGGER_PROFILES.values():
        all_triggers.update(d)
    return all_triggers


def scan_payload(payload, triggers, results):
    text = payload.decode("utf-8", errors="ignore")
    for keyword, alert in triggers.items():
        if keyword in text:
            results.append({"alert": alert, "keyword": keyword, "payload": text[:300]})


def watch_pcap(path, profile, output):
    triggers = build_trigger_set(profile)
    results = []
    count = 0
    try:
        with open(path, "rb") as f:
            pcap = dpkt.pcap.Reader(f)
            for ts, buf in pcap:
                eth = dpkt.ethernet.Ethernet(buf)
                if not isinstance(eth.data, dpkt.ip.IP):
                    continue
                ip = eth.data
                if isinstance(ip.data, dpkt.tcp.TCP):
                    tcp = ip.data
                    if tcp.data:
                        scan_payload(tcp.data, triggers, results)
                        count += 1
    except Exception as e:
        print(f"[!] Error: {e}")
        return

    for hit in results:
        print(f"[!] {hit['alert']}")
        print(f"    Payload: {hit['payload']}")
    print(f"[*] Completed. Scanned {count} TCP packets. Hits: {len(results)}")

    if output:
        with open(output, "w") as f:
            json.dump(results, f, indent=2)
        print(f"[+] Report saved to {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Path to PCAP file")
    parser.add_argument("--profile", default="all", help="Trigger profile to use")
    parser.add_argument("--output", help="Write alerts to a JSON file")
    args = parser.parse_args()
    watch_pcap(args.file, args.profile, args.output)
