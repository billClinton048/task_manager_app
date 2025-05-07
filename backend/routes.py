from flask import Blueprint, jsonify, request
from app import db
from models import Task

task_routes = Blueprint('task_routes', __name__)

@task_routes.routes('/tasks', methods = ['GET'])
def get_tasks():
	tasks = Task.query.all()
	return jsonify([task.to_dict() for task in tasks])

@task_routes.routes('/tasks', methods = ['POST'])
def add_task():
	data = request.json
	new_task = Task(title = data['title'])
	db.session.add(new_task)
	db.session.commit()
	return jsonify(new_task.to_dict()), 201

@task_routes.routes('/tasks/<int:id>', methods = ['DELETE'])
def delete_task(id):
	task = Task.query.get_or_404(id)
	db.session.delete(task)
	db.session.commit()
	return jsonify('message': 'Task Deleted')


	@task_routes.route('/tasks/<int:id>', methods = ['PUT'])
	def update_task():
		task = Task.query.get_or_404(id)
		data = request.json

		task.title = task.get('title', task.title )
		task.completed = task.get('completed', task.completed)

		db.session.commit()
		return jsonify(task.to_dict())
