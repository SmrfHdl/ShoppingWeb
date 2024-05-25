from flask import Blueprint, render_template, abort
from website.models import Product, db

pd_bp = Blueprint('pd', __name__)

@pd_bp.route("/products/<string:product_url>")
def home(product_url):
    product = db.session.query(Product).filter_by(url=product_url).first()
    if not product:
        print("Product not found")
        abort(404)  # Trả về lỗi 404 nếu không tìm thấy sản phẩm
    print("Get product information successfully")
    print(product.name)
    return render_template("products-details.html", product=product)
