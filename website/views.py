from flask import Blueprint, render_template
from flask_login import login_user, login_required, current_user

from website.models import Product

views = Blueprint('views', __name__)

@views.route('/')
# @login_required
def home():
    # Lấy ra 4 sản phẩm có lượng review_count cao nhất
    top_reviewed_products = Product.query.order_by(Product.review_count.desc()).limit(4).all()

    # Lấy ra 4 sản phẩm có rating cao nhất
    top_rated_products = Product.query.order_by(Product.rating.desc()).limit(4).all()
    return render_template("home.html", top_rated_products = top_rated_products, top_reviewed_products = top_reviewed_products)