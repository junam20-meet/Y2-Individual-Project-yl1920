from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, User


engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def add_user(username, password):
	print("Added a user!")
	user = User(username = username, password = password)
	session.add(user)
	session.commit()

def query_all_users():
	return session.query(User).all()

def query_by_name(username):
	return session.query(User).filter_by(username = username).first()














