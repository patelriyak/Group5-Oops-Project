from flask import Blueprint, render_template, request, redirect, url_for
from lib import lib
from flask import jsonify
from datetime import datetime, timedelta
from time import gmtime, strftime, mktime

caterplace_page = Blueprint("caterplace_page", __name__)

@caterplace_page.route("/caterplace", methods=["GET"])
def caterplace():
	return render_template("caterplaced.html", current=lib.current)
