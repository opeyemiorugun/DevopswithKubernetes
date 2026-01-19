from flask import render_template
from app import app
from collections import deque
import requests



def get_pongs():
    url = "http://pingpong-svc:2342/pings"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json().get("pings", 0)
    except requests.RequestException:
        return 0
    
@app.route('/')
def home(): 
    log_file_path = 'files/log_app_logs' 
    with open(log_file_path, 'r') as f:
        content  = deque(f, maxlen=1)[0]  # Keep only the last line
    counter = get_pongs()
    return render_template('index.html', contents=content, counter=counter)