import random
from datetime import datetime
import re
import mysql.connector

conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='restaurantmanagement')

class Res:

	def get_menu_list(self):
		mycursor = conn.cursor()
		mycursor.execute(f"select * from restable")
		myresult = mycursor.fetchall()
		return myresult

	def get_detail_from_name(self, name):
		mycursor = conn.cursor()
		mycursor.execute(f"select * from restable where name='{name}'")
		myresult = mycursor.fetchall()
		return myresult[0]

	def add_to_cart(self, username, foodname):
		mycursor = conn.cursor()
		val = (username, foodname)
		sql = "insert into carttable (email, foodname) values(%s, %s)"
		mycursor.execute(sql, val)
		conn.commit()
		return True

	def get_cart(self, username):
		mycursor = conn.cursor()
		mycursor.execute(f"select * from carttable where email='{username}'")
		myresult = mycursor.fetchall()
		return myresult

	def delete_cart(self, foodname, username):
		mycursor = conn.cursor()
		mycursor.execute(f"delete from carttable where email='{username}' and foodname='{foodname}'")
		conn.commit()
		return True