import re
import argparse
from collections import defaultdict
import pandas as pd

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

def export_to_csv(ip_failures, filename="failed_logins.csv"):
    df = pd.DataFrame(ip_failures.items(), columns=["IP Address", "Failed Attempts"])
    df.sort_values(by="Failed Attempts", ascending=False, inplace=True)
    df.to_csv(filename, index=False)
    print(f"\n Exported to {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze log file for failed SSH login attempts.")
    parser.add_argument("--export", action="store_true", help="Export results to CSV")

    args = parser.parse_args()

    failures = parse_log(LOG_PATH)
    print_summary(failures)

    if args.export:
        export_to_csv(failures)