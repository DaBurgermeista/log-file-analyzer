import time
import re
import os
import threading
from collections import defaultdict
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

LOG_FILE = "logs/my_auth.log"
ip_failures = defaultdict(int)

class LogEventHandler(FileSystemEventHandler):
    def __init__(self, filepath):
        self.filepath = filepath
        self._position = 0  # remember where we last read
        self.abs_filepath = os.path.abspath(filepath)
        print(f"🔍 Watching file: {self.abs_filepath}")

    def on_modified(self, event):
        if os.path.abspath(event.src_path) == self.abs_filepath:
            self.process_new_lines()

    def process_new_lines(self):
        with open(self.filepath, "r") as f:
            f.seek(self._position)
            new_lines = f.readlines()
            self._position = f.tell()

        for line in new_lines:
            if "Failed password" in line:
                match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                if match:
                    ip = match.group(1)
                    ip_failures[ip] += 1
                    print(f"[!] Failed login from {ip} — {ip_failures[ip]} total")


def print_summary():
    while True:
        time.sleep(10)
        print("\n📊 Top offending IPs:")
        if not ip_failures:
            print(" (none yet)")
            continue
        for ip, count in sorted(ip_failures.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f" - {ip}: {count} failed attempts")


if __name__ == "__main__":
    print(f"🔍 Watching for failed login attempts in: {LOG_FILE}\n")
    event_handler = LogEventHandler(LOG_FILE)
    observer = Observer()
    observer.schedule(event_handler, path="logs", recursive=False)
    threading.Thread(target=print_summary, daemon=True).start()
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
