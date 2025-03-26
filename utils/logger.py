import datetime

def log_event(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("attack.log", "a") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")

# Example Usage
if __name__ == "__main__":
    log_event("Deauth attack started on target: AA:BB:CC:DD:EE:FF")