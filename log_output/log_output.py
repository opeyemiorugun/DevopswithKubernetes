from app import app, random_id
from string_generator import logger
import threading

# start logger in background
threading.Thread(
    target=logger,
    args=(random_id,),
    daemon=True
).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
