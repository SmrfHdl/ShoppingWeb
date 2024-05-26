from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from website.models import Cart, CartItem, Order, OrderItem, Payment
from website import db

checkout_bp = Blueprint('checkout', __name__)

@checkout_bp.route('/checkout')
@login_required
def checkout():
    cart = Cart.query.filter_by(user_id=current_user.id).first()
    if not cart or cart.total_quantity == 0:
        flash('Your cart is empty!', 'warning')
        return redirect(url_for('cart.home'))
    
    return render_template('checkout.html', cart = cart)

@checkout_bp.route('/process')
def process():
    return None

# @checkout_bp.route('/place_order', methods=['POST'])
# @login_required
# def place_order():
#     cart = Cart.query.filter_by(user_id=current_user.id).first()
#     if not cart or cart.total_quantity == 0:
#         flash('Your cart is empty!', 'warning')
#         return redirect(url_for('cart.home'))
    
#     order = Order(user_id=current_user.id, total_price=cart.total_price)
#     db.session.add(order)
#     db.session.commit()
    
#     for item in cart.items:
#         order_item = OrderItem(order_id=order.id, product_id=item.product_id, quantity=item.quantity, size=item.size, price=item.product.price)
#         db.session.add(order_item)
    
#     db.session.commit()

#     payment = Payment(order_id=order.id, amount=order.total_price)
#     db.session.add(payment)
#     db.session.commit()

#     cart.items = []
#     cart.total_quantity = 0
#     cart.total_price = 0
#     db.session.commit()

#     flash('Your order has been placed successfully!', 'success')
#     return redirect(url_for('order_detail', order_id=order.id))

# @checkout_bp.route('/order_detail/<int:order_id>')
# @login_required
# def order_detail(order_id):
#     order = Order.query.get_or_404(order_id)
#     if order.user_id != current_user.id:
#         flash('You do not have permission to view this order.', 'danger')
#         return redirect(url_for('home'))
    
#     return render_template('order_detail.html', order=order)
