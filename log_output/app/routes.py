from flask import render_template
from app import app

@app.route('/')
def home():
    contents = [] 
    file_path = 'files/log_app_logs'
    with open(file_path, 'r') as f:
        contents = f.readlines() 
    return render_template('index.html', contents=contents)