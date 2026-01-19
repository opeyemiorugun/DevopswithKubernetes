from app import app 

counter = 0
def increment_counter():
    global counter
    counter += 1
    return counter
 
@app.route('/')
def index(): 
    counter = increment_counter()
    return f'pong {counter}'

@app.route('/pings')
def pings():
    return {'pings': counter}, 200