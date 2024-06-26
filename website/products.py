from flask import Blueprint, render_template, request
from website.models import Product
import pandas as pd
from website import db

products_bp = Blueprint('products', __name__)

@products_bp.route('/products')

def home():
    data = pd.read_csv('Data/final_data.csv')
    if Product.query.count() == 0:
        for index, row in data.iterrows():
            # product_ = Product(
            #     id = index + 1,
            #     name=row['Title'],
            #     price=row['Price'],
            #     rating=row['Rating'],
            #     review_count=row['Review Count'],
            #     description=row['Description'],
            #     image=row['Image_url'],
            #     category=row['Department']
            # )
            product_ = Product.create_product(row['Title'], row['Price'], row['Rating'], row['Review Count'], row['Description'], row['Image_url'], row['Department'] )
            db.session.add(product_)
        db.session.commit()

    category = request.args.get('category')

    if category:
        query = Product.query.filter_by(category=category)
        selected_category = category
    else:
        query = Product.query
        selected_category = None

    # Pagination: Thanh trượt chọn số trang
    page = request.args.get('page', 1, type=int)
    per_page = 12  # Số sản phẩm trên mỗi trang
    pagination = query.paginate(page=page, per_page=per_page)
    products = pagination.items
    print(page, per_page)

    return render_template("products.html", products=products, pagination=pagination, selected_category=selected_category)