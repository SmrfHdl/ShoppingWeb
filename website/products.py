from flask import Blueprint, render_template

products_bp = Blueprint('products', __name__)

@products_bp.route('/products')
def home():
    return render_template("products.html")