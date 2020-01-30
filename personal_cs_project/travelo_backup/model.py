from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
   __tablename__ = 'users'
   user_id = Column(Integer, primary_key=True)
   name = Column(String)
   email_adress = Column(String)
   passcode = Column(String)

   def __repr__(self):
		return ("user name:{}, user email: {}, user pass: {}".format(self.name, self.email_adress, self.passcode))







