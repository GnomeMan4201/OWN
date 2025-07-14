import dpkt, socket, time

def make_pcap(path):
    writer = dpkt.pcap.Writer(open(path, 'wb'))
    payload = b"POST /login HTTP/1.1\r\nHost: test.com\r\n\r\nusername=admin&password=secret"

    ip = dpkt.ip.IP(
        src=socket.inet_aton("10.0.0.5"),
        dst=socket.inet_aton("93.184.216.34"),
        p=dpkt.ip.IP_PROTO_TCP,
        ttl=64,
        data=dpkt.tcp.TCP(
            sport=1234,
            dport=80,
            seq=12345,
            flags=dpkt.tcp.TH_PUSH | dpkt.tcp.TH_ACK,
            data=payload
        )
    )
    ip.len = len(ip)
    eth = dpkt.ethernet.Ethernet(
        dst=b'\xaa'*6, src=b'\xbb'*6, type=dpkt.ethernet.ETH_TYPE_IP, data=ip
    )
    writer.writepkt(eth, ts=time.time())
    writer.close()

make_pcap("../logs/capture.pcap")
