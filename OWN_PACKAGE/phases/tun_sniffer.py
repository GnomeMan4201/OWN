import fcntl
import os
import select
import struct

from scapy.all import IP, wrpcap

TUNSETIFF = 0x400454CA
IFF_TUN = 0x0001
IFF_NO_PI = 0x1000
LOG_FILE = "logs/capture.pcap"


def create_tun():
    tun = os.open("/dev/net/tun", os.O_RDWR)
    ifr = struct.pack("16sH", b"tun0", IFF_TUN | IFF_NO_PI)
    fcntl.ioctl(tun, TUNSETIFF, ifr)
    return tun


def run_sniffer():
    tun = create_tun()
    print("[*] TUN interface created. Listening for packets...")
    packets = []
    try:
        while True:
            r, _, _ = select.select([tun], [], [])
            if tun in r:
                pkt = os.read(tun, 2048)
                p = IP(pkt)
                packets.append(p)
                print(f"[+] Captured: {p.summary()}")
    except KeyboardInterrupt:
        print(f"\n[*] Saving to {LOG_FILE}")
        wrpcap(LOG_FILE, packets)


if __name__ == "__main__":
    run_sniffer()
