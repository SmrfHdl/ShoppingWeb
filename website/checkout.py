from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, current_user, login_required
from website.models import Cart, CartItem, Order, OrderItem, Payment, User
from website import db
from datetime import datetime

checkout_bp = Blueprint('checkout', __name__)

@checkout_bp.route('/checkout')
@login_required
def checkout():
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    if not cart or cart.total_quantity == 0:
        flash('Your cart is empty!', 'warning')
        return redirect(url_for('cart.home'))
    
    return render_template('checkout.html', cart = cart)

@checkout_bp.route('/process', methods=['POST'])
def process():
    if current_user.cart is not None:
        items = current_user.cart.items
    else:
        print("Cart does not exist.")
    # Kiểm tra xem người dùng đã đăng nhập chưa
    if not current_user.is_authenticated:
        flash('Please log in to proceed with payment.', 'warning')
        return redirect(url_for('account.home'))
    
    else: 
        # Nhận thông tin từ form thanh toán
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        address = request.form.get('address')

        print(name, phone, email, address)

        db.session.add(Cart(user_id=current_user.id))
        db.session.commit()

        # Tạo đối tượng Order dựa trên thông tin đơn hàng của người dùng
        order = Order(user_id=current_user.id, order_date=datetime.utcnow(), status='Pending')

        # Lặp qua từng mục trong giỏ hàng của người dùng và tạo đối tượng OrderItem cho mỗi mục
        for cart_item in current_user.cart.items:
            order_item = OrderItem(order_id=order.id, product_id=cart_item.product_id, quantity=cart_item.quantity, size=cart_item.size, price=cart_item.product.price)
            db.session.add(order_item)

        # Tính tổng số tiền của đơn hàng
        total_price = sum(item.product.price * item.quantity for item in current_user.cart.items)

        order.total_price = total_price
        db.session.add(order)
        db.session.flush()  # Lấy id của order mới tạo

        # Tạo đối tượng Payment để lưu thông tin về thanh toán
        payment = Payment(order_id=order.id, amount=total_price, payment_date=datetime.utcnow(), status='Completed')
        db.session.add(payment)

        # Xóa giỏ hàng của người dùng sau khi đã thanh toán
        current_user.cart.items.clear()
        db.session.commit()

        flash('Payment successful! Thank you for your purchase.', 'success')
        return redirect(url_for('checkout'))