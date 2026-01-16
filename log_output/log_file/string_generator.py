import time
import uuid
from datetime import datetime, timezone

random_id = str(uuid.uuid4())
file_path = 'files/log_app_logs'


while True:
    timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    with open(file_path, 'a') as f:
        f.write(f"{timestamp}: {random_id}\n")
    time.sleep(5)