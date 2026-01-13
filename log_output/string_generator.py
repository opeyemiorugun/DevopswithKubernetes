import time
from datetime import datetime, timezone


def logger(random_id):
    while True:
        timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        print(f"{timestamp}: {random_id}", flush=True)
        time.sleep(5)
    
    