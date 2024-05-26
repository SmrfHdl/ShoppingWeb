from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from website.models import Product, Cart, CartItem
from flask_login import current_user
from website import db

pd_bp = Blueprint('pd', __name__)

@pd_bp.route("/products/<string:product_url>")
def home(product_url):
    product = Product.query.filter_by(url=product_url).first()
    if not product:
        print("Product not found")
        abort(404)  # Trả về lỗi 404 nếu không tìm thấy sản phẩm
    print("Get product information successfully")
    print(product.name)
    return render_template("products-details.html", product=product)

@pd_bp.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if not current_user.is_authenticated:
        flash('Please log in to add items to your cart.', 'warning')
        return redirect(url_for('account.home'))
    
    product = Product.query.get_or_404(product_id)
    size = request.form.get('size')
    quantity = request.form.get('quantity', type=int)
    print(product.name, quantity, size)

    if not size:
        flash('Please select a size.', 'warning')
        return redirect(url_for('pd.home', product_url=product.url))
    
    if quantity < 1:
        flash('Quantity must be at least 1.', 'warning')
        return redirect(url_for('pd.home', product_url=product.url))
    
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    if not cart:
        cart = Cart(user_id=current_user.id)
        db.session.add(cart)

    try:
        # Bắt đầu một phiên giao dịch mới
        # Thực hiện các thao tác trên cơ sở dữ liệu
        if not db.session.is_active:
            db.session.begin()

        cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product.id, size=size).first()
        if cart_item:
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(cart_id=cart.id, product_id=product.id, quantity=quantity, size=size)
            db.session.add(cart_item)

        # db.session.commit()  # Lưu thay đổi vào cơ sở dữ liệu

        cart.update_totals()

        flash('Item added to cart!', 'success')
    except Exception as e:
        # db.session.rollback()  # Rollback lại giao dịch nếu có lỗi
        flash('An error occurred. Please try again.', 'danger')
        print("Error adding item to cart:", e)
    
    return redirect(url_for('pd.home', product_url=product.url))
