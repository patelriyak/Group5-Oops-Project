from flask import Blueprint, render_template, request, redirect, url_for
from flask import jsonify
from lib import lib
from model.res import Res
from model.user import User
from datetime import datetime, timedelta
from time import gmtime, strftime, mktime

res_page = Blueprint("res_page", __name__)
model_res = Res()
model_user = User()

@res_page.route("/home/", methods=["GET"])
def home():
	print(lib.username)
	return render_template("home.html", current=lib.current)

@res_page.route("/res_list/", methods=["GET"])
def res_list():
	data = model_res.get_menu_list()
	return render_template("res_list.html", data=data, current=lib.current)

@res_page.route("/my_cart/", methods=["GET"])
def my_cart():
	data = model_res.get_cart(lib.username)
	details = []
	for i in range(len(data)):
		details.append(model_res.get_detail_from_name(data[i][2]))
	return render_template("my_cart.html", data=details, current=lib.current)

@res_page.route("/add_cart/", methods=["GET"])
def res_add_cart():
	req = request.values
	data = model_res.get_detail_from_name(req['name'])
	return render_template("res_add_cart.html", data=data, current=lib.current)

@res_page.route("/add_cart/", methods=["POST"])
def res_add_cart_post():
	foodname = request.form.get('foodname')
	model_res.add_to_cart(lib.username, foodname)
	data = model_res.get_detail_from_name(foodname)
	return render_template("res_checkout.html", data=data, current=lib.current)

@res_page.route("/checkout/", methods=["GET"])
def rest_checkout():
	foodname = request.values['name']
	data = model_res.get_detail_from_name(foodname)
	return render_template("res_checkout.html", data=data, current=lib.current)

@res_page.route("/checkout/", methods=["POST"])
def res_checkout_post():
	foodname = request.form.get('foodname')
    print(foodname);             
	model_res.delete_cart(foodname, lib.username)
	data = model_res.get_detail_from_name(foodname)
    print('1')    
    print(lib.username)               
	print(lib.current)
	print(data[2])
	remaining = round(lib.current - float(data[2]), 2)
	lib.current = remaining
	model_user.update_budget(lib.username, remaining)
	return redirect(url_for('res_page.my_cart'))