from flask import Flask, render_template_string, jsonify, request  
from flask_cors import CORS
import os
import sqlalchemy as sa

app = Flask(__name__) 
CORS(app)

database_url = os.getenv("POSTGRES_URL")
engine = sa.create_engine(database_url)
metadata = sa.MetaData()
todos = sa.Table(
	'todos',
	metadata,
	sa.Column("id", sa.Integer, primary_key=True),
	sa.Column('task', sa.String, nullable=False, unique=True)
)
metadata.create_all(engine)

def get_all_todos():
	with engine.connect() as conn:
		result = conn.execute(sa.select(todos.c.task)).scalars().all()
	todo_list = result if result is not None else []
	return todo_list

def insert_todo(task):
	with engine.begin() as conn:
		conn.execute(todos.insert().values(task=task))
    
@app.route('/todos',methods=['GET', 'POST'])
def home():
	list_of_todos = get_all_todos()
	if request.method == "GET":
		return render_template_string('''
			{% for todo in todos %}
				<li>{{ todo }}</li>
			{% endfor %}
		''', todos=list_of_todos), 200
	else:
		task = request.form.get('todo', '').strip()

		if not task:
			return "<p>Todo cannot be empty!</p>", 400
		try:
			insert_todo(task)
			return f"<li>{task}</li>", 200
		except sa.exc.IntegrityError:
			return "<p>Todo already exists!</p>", 409
 