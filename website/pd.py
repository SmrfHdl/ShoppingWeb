from flask import Blueprint, render_template

pd = Blueprint('pd', __name__)

@pd.route('/')
def home():
    return render_template("products-details.html")