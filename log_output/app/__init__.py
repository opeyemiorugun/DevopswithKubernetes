from flask import Flask
import uuid

app = Flask(__name__) 

random_id = str(uuid.uuid4())

from app import routes