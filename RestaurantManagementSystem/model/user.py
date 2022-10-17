import random
from datetime import datetime
import re
import mysql.connector

conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='restaurantmanagement')

class User:

	def validate_username(self, username, password):
		mycursor = conn.cursor()
		mycursor.execute(f"select * from usertable where email='{username}' and password='{password}'")
		myresult = mycursor.fetchall()
		if len(myresult) >= 1:
			return myresult[0][1]
		return ""

	def getRole(self, username):
		mycursor = conn.cursor()
		mycursor.execute(f"select role from usertable where email='{username}'")
		myresult = mycursor.fetchall()
		return myresult[0][0]

	def get_current(self, username):
		mycursor = conn.cursor()
		mycursor.execute(f"select budget from usertable where email='{username}'")
		myresult = mycursor.fetchall()
		return myresult[0][0]

	def validate_register(self, username):
		mycursor = conn.cursor()
		mycursor.execute(f"select * from usertable where email='{username}'")
		myresult = mycursor.fetchall()
		if len(myresult) < 1:
			return True
		return False

	def register_user(self, username, password, role):
		mycursor = conn.cursor()
		val = (username, password, role)
		sql = "insert into usertable (email, password, role) values(%s, %s, %s)"
		mycursor.execute(sql, val)
		conn.commit()
		return True

	def forget_user(self, username):
		mycursor = conn.cursor()
		mycursor.execute(f"select role from usertable where email='{username}'")
		myresult = mycursor.fetchall()
		if len(myresult) > 0:
			return True
		return False

	def forget_password(self, username, password):
		mycursor = conn.cursor()
		mycursor.execute(f"update usertable set password='{password}' where email='{username}'")
		conn.commit()
		return True

	def update_budget(self, username, budget):
		mycursor = conn.cursor()
		mycursor.execute(f"update usertable set budget='{budget}' where email='{username}'")
		conn.commit()
		return True
