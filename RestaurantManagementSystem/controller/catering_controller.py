from ssl import CertificateError
from flask import Blueprint, render_template, request, redirect, url_for, redirect
from lib import lib
from flask import jsonify
from datetime import datetime, timedelta
from time import gmtime, strftime, mktime
import random
import re
import mysql.connector

conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='restaurantmanagement')

catering_page = Blueprint("catering_page", __name__)


@catering_page.route("/catering", methods=["GET","POST"])
def add_catering():
	if request.method == 'POST':
		caterDetails = request.form
		firstname = caterDetails['firstname']
		lastname = caterDetails['lastname']
		email = caterDetails['email']
		contactnumber = caterDetails['contactnumber']
		items = caterDetails['items']
		cateringdate = caterDetails['cateringdate']
		venue = caterDetails['venue']
		specialinstructions = caterDetails['specialinstructions']
		mycursor = conn.cursor()
		mycursor.execute("insert into catertable (firstname, lastname, email, contactnumber, items, cateringdate, venue, specialinstructions) values(%s, %s, %s, %s, %s, %s, %s, %s)",(firstname,lastname,email,contactnumber,items,cateringdate,venue,specialinstructions))
		conn.commit()
		mycursor.close()
		print (caterDetails)
		return redirect('/caterplace')
	return render_template("catering.html")

@catering_page.route("/caterplace")
def caterplace():
	print("catreplace")
	mycursor = conn.cursor()
	cater_value = mycursor.execute("SELECT * FROM catertable")
	if cater_value > 0:
		print("true")
		caterDetails = mycursor.fetchall()
		print(caterDetails)
		return render_template("caterplaced.html", caterDetails = caterDetails)
	else:
		print("false")