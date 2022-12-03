from flask import Blueprint, render_template, request, redirect, url_for
from lib import lib
from flask import jsonify
from datetime import datetime, timedelta
from time import gmtime, strftime, mktime

gallery_page = Blueprint("gallery_page", __name__)

@gallery_page.route("/gallery", methods=["GET"])
def gallery():
	return render_template("gallery.html", current=lib.current)