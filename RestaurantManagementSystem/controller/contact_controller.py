from flask import Blueprint, render_template, request, redirect, url_for
from lib import lib
from flask import jsonify
from datetime import datetime, timedelta
from time import gmtime, strftime, mktime

contact_page = Blueprint("contact_page", __name__)

@contact_page.route("/contact", methods=["GET"])
def contact():
	return render_template("contact.html", current=lib.current)