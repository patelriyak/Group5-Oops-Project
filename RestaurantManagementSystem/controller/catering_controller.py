from flask import Blueprint, render_template, request, redirect, url_for
from lib import lib
from flask import jsonify
from datetime import datetime, timedelta
from time import gmtime, strftime, mktime

catering_page = Blueprint("catering_page", __name__)

@catering_page.route("/catering", methods=["GET"])
def catering():
	return render_template("catering.html", current=lib.current)