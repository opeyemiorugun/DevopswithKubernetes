from flask import render_template
from app import app, random_id
from datetime import datetime, timezone

@app.route('/')
def home():
    current_time = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    return f"{current_time}: {random_id}"