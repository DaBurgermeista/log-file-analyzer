from scapy.all import sniff, IP
from collections import defaultdict
from datetime import datetime

traffic_count = defaultdict(int)

def process_packet(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst
        traffic_count[src] += 1
        traffic_count[dst] += 1
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {src} → {dst}")

def print_summary():
    print("\n📊 IP Traffic Summary:")
    for ip, count in sorted(traffic_count.items(), key=lambda x: x[1], reverse=True):
        print(f" - {ip}: {count} packets")

if __name__ == "__main__":
    print("🛡️  Sniffing IP traffic (press Ctrl+C to stop)...\n")
    try:
        sniff(filter="ip", prn=process_packet, store=0)
    except KeyboardInterrupt:
        print_summary()
