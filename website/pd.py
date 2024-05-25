from flask import Blueprint, render_template, abort
from website.models import Product, db
# Import for Recommendation System
# from RecommendationSystem.CBCF_function import get_CF_data
# from RecommendationSystem.collaborative_filtering import CF

pd_bp = Blueprint('pd', __name__)

@pd_bp.route("/products/<string:product_url>")
def home(product_url):

    # data = get_CF_data("instance\database.db") #ub.base là file chứa rating của một số user về các sản phẩm. mỗi user đã rating ít nhất 10 sản phẩm
    # test = CF(data,5)
    # test.fit()


    product = db.session.query(Product).filter_by(url=product_url).first()
    if not product:
        print("Product not found")
        abort(404)  # Trả về lỗi 404 nếu không tìm thấy sản phẩm
    print("Get product information successfully")
    print(product.name)
    return render_template("products-details.html", product=product)
