from flask import Flask

app = Flask(__name__)
counter = 0 

from app import routes