from flask import render_template
from app import app
from collections import deque

@app.route('/')
def home():
    contents = [] 
    log_file_path = 'files/log_app_logs'
    ping_file_path = 'files/pingpong_counter'
    with open(log_file_path, 'r') as f:
        content  = deque(f, maxlen=1)[0]  # Keep only the last line
    with open(ping_file_path, 'r') as f:
        counter = f.read().strip()
    return render_template('index.html', contents=content, counter=counter)