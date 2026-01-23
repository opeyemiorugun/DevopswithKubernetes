import os
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
env_var = os.getenv("MESSAGE")

@app.route('/')
def home(): 
    log_file_path = 'files/log_app_logs'
    info_file_path = 'config/information.txt'
    with open(log_file_path, 'r') as f, open(info_file_path, 'r') as info_file:
        content  = deque(f, maxlen=1)[0]  # Keep only the last line
        info_content = info_file.read()
    counter = get_pongs()
    return render_template('index.html', contents=content, counter=counter, info_content=info_content, env_var=env_var)