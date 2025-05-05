from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)

	with app.app_context():
		from models import Task
		db.create_all()

		from routes import task_routes
		app.register_blueprint(task_routes)

	return app

if __name__ =='__main__':
	app = create_app()
	app.run(debug= True)
