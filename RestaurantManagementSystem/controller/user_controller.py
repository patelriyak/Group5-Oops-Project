from flask import Blueprint, render_template, request, redirect, url_for
from lib import lib
from model.user import User
from flask import jsonify
from datetime import datetime, timedelta
from time import gmtime, strftime, mktime

user_page = Blueprint("user_page", __name__)

model_user = User()

@user_page.route("/", methods=["GET"])
def login_index():
	return render_template("login.html")

@user_page.route("/login", methods=["GET"])
def login():
	return render_template("login.html")

@user_page.route("/login", methods=["POST"])
def login_post():
	username = request.form.get('username')
	password = request.form.get('password')


	# user exist
	if model_user.validate_username(username, password) != "":
		# if client
		if model_user.getRole(username) == 1:
			lib.username = model_user.validate_username(username, password)
			lib.current = model_user.get_current(username)
			return redirect(url_for('res_page.home'))
		# if admin
		else:
			return "Admin"
	
	# if user not exist
	error = 'Invalid username/password. Please try again.'
	return render_template("login.html", error=error)

@user_page.route("/signup", methods=["GET"])
def signup():
	return render_template("signup.html")

@user_page.route("/signup", methods=["POST"])
def signup_post():
	username = request.form.get('username')
	password = request.form.get('password')
	confirm = request.form.get('confirm')

	if password == confirm and model_user.validate_register(username):
		if model_user.register_user(username, password, 1):
			return redirect(url_for('user_page.login'))

	return render_template("signup.html")

@user_page.route("/forget", methods=["GET"])
def forget():
	return render_template("forget.html")

@user_page.route("/forget", methods=["POST"])
def forget_post():
	username = request.form.get('username')
	lib.username = username
	if model_user.forget_user(username):
		return redirect(url_for('user_page.forgetpassword'))
	return render_template("forget.html")

@user_page.route("/forgetpassword", methods=["GET"])
def forgetpassword():
	return render_template("forgetpassword.html")

@user_page.route("/forgetpassword", methods=["POST"])
def forgetpassword_post():
	password = request.form.get('password')
	if model_user.forget_password(lib.username, password):
		return redirect(url_for('user_page.login'))
	return render_template("forgetpassword.html")

@user_page.route("/logout", methods=["GET"])
def logout():
	lib.username = None
	return redirect(url_for('user_page.login'))