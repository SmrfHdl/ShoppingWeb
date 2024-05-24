from flask import Blueprint, render_template

pd_bp = Blueprint('pd', __name__)

@pd_bp.route('/products_details')
def home():
    return render_template("products-details.html")