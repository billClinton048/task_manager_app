from app import db

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(200), nullable = False)
	completed = db.Column(db.Boolean, default = False)

def to_dict(self):
	return {
	'id' : self.id,
	'title' : self.title,
	'completed' : self.completed
	}