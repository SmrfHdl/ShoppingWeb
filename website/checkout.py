from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from website.models import Product, Cart, CartItem, Order, OrderItem, Payment
from website import db
from datetime import datetime

checkout_bp = Blueprint('checkout', __name__)

@checkout_bp.route('/checkout')
@login_required
def home():
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    if not cart or cart.total_quantity == 0:
        flash('Your cart is empty!', 'warning')
        return redirect(url_for('cart.home'))
    
    return render_template('checkout.html', cart = cart, current_user=current_user)

@checkout_bp.route('/payment', methods=['GET', 'POST'])
def payment():
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    if not cart or cart.total_quantity == 0:
        flash('Your cart is empty!', 'warning')
        return redirect(url_for('cart.home'))
    
    if request.method == 'POST':
        # Lấy thông tin từ form
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        address = request.form.get('address')

        # Kiểm tra số dư của người dùng
        if current_user.balance < cart.total_price:
            flash('Insufficient balance to complete the purchase.', 'danger')
            return redirect(url_for('checkout.home'))

        # Trừ số dư tài khoản người dùng
        current_user.balance -= cart.total_price

        # Tạo đơn hàng mới
        order = Order(
            user_id=current_user.id,
            order_date=datetime.utcnow(),
            status='Pending',
            total_price=cart.total_price,
            email=email,
            name=name,
            address=address,
            phone=phone
        )
        
        db.session.add(order)
        db.session.commit()  # Commit để lấy ID cho order

        # Tạo các mục OrderItem từ CartItem
        for cart_item in cart.items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=cart_item.product_id,
                quantity=cart_item.quantity,
                size=cart_item.size,
                price=cart_item.product.price
            )
            db.session.add(order_item)

        # Tạo Payment
        payment = Payment(
            order_id=order.id,
            amount=order.total_price,
            payment_date=datetime.utcnow(),
            status='Completed'
        )
        db.session.add(payment)

        # Xóa các mục CartItem và cập nhật giỏ hàng
        for cart_item in cart.items:
            db.session.delete(cart_item)
        cart.total_quantity = 0
        cart.total_price = 0

        db.session.commit()

        flash('Your order has been placed successfully!', 'success')
    return redirect(url_for('views.home'))