import time
import random

ips = ["192.168.0.25", "10.0.0.12", "172.16.0.5", "203.0.113.8"]
users = ["admin", "testuser", "root", "guest"]
log_path = "logs/my_auth.log"

with open(log_path, "a") as f:
    for i in range(20):
        ip = random.choice(ips)
        user = random.choice(users)
        port = random.randint(50000, 60000)
        pid = random.randint(10000, 99999)
        line = f"Jun 20 15:{random.randint(10,59)}:01 server sshd[{pid}]: Failed password for {user} from {ip} port {port} ssh2\n"
        f.write(line)
        f.flush()
        print(f"[+] {line.strip()}")
        time.sleep(1)
