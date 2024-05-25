from flask import Blueprint, render_template
from website.models import Product
import pandas as pd
from website import db

products_bp = Blueprint('products', __name__)

@products_bp.route('/products')

def home():
    data = pd.read_csv('Data/final_data.csv')
    max_id = db.session.query(db.func.max(Product.id)).scalar() or 0
    if Product.query.count() == 0:
        for index, row in data.iterrows():
            existing_product = Product.query.filter_by(name=row['Title'], price=row['Price']).first() 
            if existing_product is None:
                product_ = Product(
                    id = max_id + index + 1,
                    name=row['Title'],
                    price=row['Price'],
                    rating=row['Rating'],
                    review_count=row['Review Count'],
                    description=row['Description'],
                    image=row['Image_url'],
                    category=row['Department']
                )
                db.session.add(product_)
        db.session.commit()
    product = Product.query.all()
    return render_template("products.html", products=product)