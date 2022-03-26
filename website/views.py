from flask import Blueprint

views = Blueprint("views", __name__)

@views.route("/") #decorater - defines the home page as indicated by /
def home():
    return  "<h1>Test</h1>"