from flask import Blueprint, render_template
from .models import Product

products_bp = Blueprint('products', __name__)

@products_bp.route('/products')
def home():
    products = Product.query.all()
    return render_template("products.html", products=products)