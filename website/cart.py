from flask import Blueprint, render_template

cart = Blueprint('cart', __name__)

@cart.route('/')
def home():
    return render_template("cart.html")