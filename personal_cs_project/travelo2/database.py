# from model import *
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker


# engine = create_engine('sqlite:///lecture.db')
# Base.metadata.create_all(engine)
# DBSession = sessionmaker(bind=engine)
# session = DBSession()



# def add_user(name, email_adress, passcode):
#     """

#     """
#     student_object = Student(
#         name=name,
#         year=email_adress,
#         passcode= passcode)
#     session.add(user_object)
#     session.commit()


from model import Base, Product

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_product(name , price , picture_link, description):
	product_object = Product(
        					name=name,
        					price = price,
        					picture_link=picture_link,
        					description=description)
	session.add(product_object)
	session.commit()
    
add_product("iphone", 3000,"https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwi7vqb1oY3mAhVF4OAKHWtLBXQQjRx6BAgBEAQ&url=https%3A%2F%2Fwww.delish.com%2Fholiday-recipes%2Fchristmas%2Fg2177%2Feasy-christmas-cookies%2F&psig=AOvVaw1VRyiuEAQum-eZt4tnIS7-&ust=1575042830567193", "beautiful iphone")



def delete_product(the_name):
	session.query(Product).filter_by(
    	name=the_name).delete()
	session.commit()


def update_product(name,price,picture_link,description):
	product = session.query(Product).filter_by(
		name=name).first()
	product.name = name
	product.price = price
	product.picture_link = picture_link
	product.description = description

	session.commit()




def quere_all():
	product = session.query(
    	Student).all()
	return students



def query_by_name(the_name):
	product1 = session.query(
		Product).filter_by(
		name=the_name).first()
	return Product1




def add_to_cart(productID):
	productID_object = cart(
		productID=productID)
	session.add(productID_object)
	session.commit()






