from app import app, counter

@app.route('/')
def index():
    global counter # Declare intent to make it a global variable so it can be modified.
    counter += 1
    return f'pong {counter}'