import uuid
import time
from datetime import datetime, timezone

random_id = str(uuid.uuid4())

while True:
    timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    print(f"{timestamp}: {random_id}", flush=True)
    time.sleep(5)