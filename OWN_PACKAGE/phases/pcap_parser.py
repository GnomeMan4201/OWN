import argparse
import json
import socket

import dpkt


def analyze_pcap(filename, output_json=False):
    results = []
    try:
        with open(filename, "rb") as f:
            pcap = dpkt.pcap.Reader(f)
            count = 0
            for ts, buf in pcap:
                eth = dpkt.ethernet.Ethernet(buf)
                if not isinstance(eth.data, dpkt.ip.IP):
                    continue
                ip = eth.data
                if isinstance(ip.data, dpkt.tcp.TCP):
                    tcp = ip.data
                    if len(tcp.data) == 0:
                        continue
                    payload = tcp.data.decode(errors="ignore")
                    if "POST" in payload or "GET" in payload:
                        packet_info = {
                            "packet": count + 1,
                            "source_ip": socket.inet_ntoa(ip.src),
                            "http": payload[:300],
                        }
                        if "password" in payload or "login" in payload:
                            packet_info["credentials_found"] = True
                        results.append(packet_info)
                    count += 1
            if output_json:
                print(json.dumps(results, indent=2))
            else:
                for r in results:
                    print(f"[+] Packet #{r['packet']}")
                    print(f"    Source IP: {r['source_ip']}")
                    print(f"    HTTP Request Detected:\n{r['http']}")
                    if r.get("credentials_found"):
                        print("    [!] Credential Keywords Found!")
            print(f"[*] Completed. Parsed {count} packets.")
    except Exception as e:
        print(f"[!] Error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--file", default="../logs/capture.pcap", help="Path to PCAP file"
    )
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()
    analyze_pcap(args.file, output_json=args.json)
