import os

class Config:
	SECRET_KEY = 'Key'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///tasks.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False