from flask import render_template
from app import app
import requests
import random
import string
from pathlib import Path
from threading import Timer, Lock
import os



class ImageManager:
    def __init__(self):
        self.baseurl = os.getenv("IMAGE_SERVICE_URL", "https://picsum.photos/200/300")
        self.images_rendered = []  
        self.directory = Path("./app/static")
        self.timer_finish = False
        self.TIMER_INTERVAL = int(os.getenv("TIMER_INTERVAL", 600))  # Default to 10 minutes
        self.lock = Lock()

    def generate_img_name(self):
        print("Generating image name.")
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choices(characters, k=10))
        return f"img_{random_string}.jpg"

    def download_image(self):
        print("Downloading new image.")
        response = requests.get(self.baseurl)
        response.raise_for_status()  # Check if the request was successful
        img_name = self.generate_img_name() 
        img_path = self.directory / img_name
        with open(img_path, "wb") as f:
            f.write(response.content)
        self.images_rendered.append(img_path) 
        return img_path

    def get_random_image(self):
        if not any(self.directory.iterdir()):
            return self.download_image()
        
        available_images = [f for f in self.directory.iterdir() if f.is_file() and f not in self.images_rendered] 
        if available_images: 
            img_file = random.choice(available_images)
            self.images_rendered.append(img_file)
            return img_file
        else:
            # All images have been rendered, download a new one 
            return self.download_image()

    def image_to_render(self): 
        with self.lock: 
            if self.timer_finish:
                self.timer_finish = False
                image = self.get_random_image()
            elif not self.images_rendered:
                image = self.get_random_image()    
            else:
                image = self.images_rendered[-1]
            return image    

    def timer_finished(self): 
        with self.lock:
            self.timer_finish = True
        self.start_timer()
    
    def  start_timer(self):
        self.timer = Timer(self.TIMER_INTERVAL, self.timer_finished)
        self.timer.daemon = True   
        self.timer.start() 
    
# Create the manager instance
image_manager = ImageManager()
 
image_manager.start_timer() 
baseurl = os.getenv("TODO_API_URL")
# baseurl = "http://localhost:5001/todos"


@app.route('/')
def home():
    random_img = image_manager.image_to_render()
    return render_template('index.html', image_path=random_img, URL=baseurl)

