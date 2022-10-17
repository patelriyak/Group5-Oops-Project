from flask import Blueprint, render_template, request, redirect, url_for
from lib import lib
from flask import jsonify
from datetime import datetime, timedelta
from time import gmtime, strftime, mktime

about_page = Blueprint("about_page", __name__)

@about_page.route("/about", methods=["GET"])
def about():
	return render_template("about.html", current=lib.current)