from flask import Flask, render_template_string, jsonify, request  
from flask_cors import CORS

app = Flask(__name__) 
CORS(app)
 
 
list_of_todos = []
    
@app.route('/todos',methods=['GET', 'POST'])
def home():
	if request.method == "GET":
		return render_template_string('''
			{% for todo in todos %}
				<li>{{ todo }}</li>
			{% endfor %}
		''', todos=list_of_todos), 200
	else:
		if request.form['todo'] in list_of_todos:
			return "<p>Todo already exists!</p>", 409
		elif not request.form['todo'].strip():
			return "<p>Todo cannot be empty!</p>", 400
		list_of_todos.append(request.form['todo'])
		return f"<li>{request.form['todo']}</li>", 200
 