import socket
import time

import dpkt


def create_pcap(filename):
    pcap_writer = dpkt.pcap.Writer(open(filename, "wb"))

    eth_type = b"\x00\x00"  # dummy
    ts = time.time()

    ip = dpkt.ip.IP(
        src=socket.inet_aton("10.0.0.5"),
        dst=socket.inet_aton("93.184.216.34"),
        p=dpkt.ip.IP_PROTO_TCP,
        data=dpkt.tcp.TCP(
            sport=12345,
            dport=80,
            seq=1000,
            ack=0,
            flags=dpkt.tcp.TH_PUSH | dpkt.tcp.TH_ACK,
            data=b"username=admin&password=admin123",
        ),
    )
    ip.len = len(ip)
    eth = b"\x00" * 14 + bytes(ip)

    pcap_writer.writepkt(eth, ts)
    pcap_writer.close()


create_pcap("../logs/capture.pcap")
