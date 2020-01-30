'''from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()'''

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
   __tablename__ = 'users'
   user_id = Column(Integer, primary_key=True)
   username = Column(String)
   password = Column(String)

   def __repr__(self):
		return ("user username:{}, user password: {}".format(self.username, self.password))






