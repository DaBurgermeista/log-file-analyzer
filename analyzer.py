import re
from collections import defaultdict

LOG_PATH = "logs/sample_auth.log"

def parse_log(file_path):
    ip_failures = defaultdict(int)

    with open(file_path, "r") as f:
        for line in f:
            if "Failed password" in line:
                match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                if match:
                    ip = match.group(1)
                    ip_failures[ip] += 1
    
    return ip_failures

def print_summary(ip_failures):
    print("Failed Login Attempts by IP:\n")
    for ip, count in sorted(ip_failures.items(), key=lambda x: x[1], reverse=True):
        print(f"{ip}: {count} failed attempts")

if __name__ == "__main__":
    failures = parse_log(LOG_PATH)
    print_summary(failures)