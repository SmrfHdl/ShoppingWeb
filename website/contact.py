from flask import Blueprint, render_template

contact = Blueprint('contact', __name__)

@contact.route('/')
def home():
    return render_template("contact.html")