from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from website.models import Product, Cart, CartItem
from flask_login import current_user
from website import db
from sqlalchemy.sql.expression import func
import RecommendationSystem.content_based as RCM_content_based

pd_bp = Blueprint('pd', __name__)

@pd_bp.route("/products/<string:product_url>")
def home(product_url):
    product = Product.query.filter_by(url=product_url).first()
    if not product:
        print("Product not found")
        abort(404)  # Trả về lỗi 404 nếu không tìm thấy sản phẩm
    print("Get product information successfully")

    number_of_recommended_products = 4
    # rcm_products = Product.query.filter_by(category=product.category)\
    #                             .filter(Product.id != product.id)\
    #                             .order_by(func.random())\
    #                             .limit(number_of_recommended_products)\
    #                             .all()
    # Giả sử bạn có hàm get_recommended_product_ids trả về danh sách các ID sản phẩm đề xuất
    recommended_ids = RCM_content_based.get_recommendations(product.name, number_of_recommended_products)
    
    # Lấy các sản phẩm từ danh sách ID đề xuất
    rcm_products = Product.query.filter(Product.id.in_(recommended_ids)).all()
    
    return render_template("products-details.html", product=product, rcm_products=rcm_products)

@pd_bp.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if not current_user.is_authenticated:
        flash('Please log in to add items to your cart.', 'warning')
        return redirect(url_for('account.home'))
    
    product = Product.query.get_or_404(product_id)
    size = request.form.get('size')
    quantity = request.form.get('quantity', type=int)
    print(product.id, product.name, quantity, size)

    if not size:
        flash('Please select a size.', 'warning')
        return redirect(url_for('pd.home', product_url=product.url))
    
    if quantity < 1:
        flash('Quantity must be at least 1.', 'warning')
        return redirect(url_for('pd.home', product_url=product.url))
    
    cart = Cart.query.filter_by(user_id=current_user.id).first()

    if cart:
        cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product.id, size=size).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(cart_id=cart.id, product_id=product.id, quantity=quantity, size=size)
            db.session.add(cart_item)
            
        db.session.commit()

        cart.update_totals()

        flash('Item added to cart!', 'success')
    else:
        flash('Cart not found.', 'danger')
    
    return redirect(url_for('pd.home', product_url=product.url))
