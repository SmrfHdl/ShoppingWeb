from flask import Blueprint, render_template

products = Blueprint('products', __name__)

@products.route('/')
def home():
    return render_template("products.html")