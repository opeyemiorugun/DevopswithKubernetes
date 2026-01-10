from app import app

@app.route('/')
def home():
    return f'Server started in port {app.config["PORT"]}'