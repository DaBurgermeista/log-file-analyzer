import time
import re
from collections import defaultdict
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

LOG_FILE = "logs/sample_auth.log"
ip_failures = defaultdict(int)

class LogEventHandler(FileSystemEventHandler):
    def __init__(self, filepath):
        self.filepath = filepath
        self._position = 0  # remember where we last read

    def on_modified(self, event):
        if event.src_path.endswith(self.filepath):
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

if __name__ == "__main__":
    print(f"🔍 Watching for failed login attempts in: {LOG_FILE}\n")
    event_handler = LogEventHandler(LOG_FILE)
    observer = Observer()
    observer.schedule(event_handler, path="logs", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
