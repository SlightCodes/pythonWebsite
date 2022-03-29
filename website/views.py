from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/") #decorater - defines the home page as indicated by /
def home():
    return  render_template("home.html")