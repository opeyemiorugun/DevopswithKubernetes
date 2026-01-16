from app import app, counter

@app.route('/')
def index():
    global counter # Declare intent to make it a global variable so it can be modified.
    counter += 1
    file_path = 'temp/pingpong_counter'
    with open(file_path, 'w') as f:
        f.write(str(counter)) 
    return f'pong {counter}'