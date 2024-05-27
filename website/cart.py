from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from website.models import Cart, CartItem
from website import db

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/home')
def home():
    if not current_user.is_authenticated:
        flash('Please log in to view your cart.', 'warning')
        return redirect(url_for('account.home'))
    else:
        cart = Cart.query.filter_by(user_id=current_user.id).first()
        db.session.add(cart)
        db.session.commit()
        return render_template('cart.html', cart = cart)

@cart_bp.route('/update_quantity', methods=['POST'])
@login_required
def update_quantity():
    item_id = request.form.get('item_id', type=int)
    new_quantity = request.form.get('quantity', type=int)

    cart_item = CartItem.query.get_or_404(item_id)
    if cart_item.cart.user_id != current_user.id:
        flash('You do not have permission to update this item.', 'danger')
        return redirect(url_for('cart.home'))

    cart_item.quantity = new_quantity
    db.session.add(cart_item)
    db.session.commit()
    cart_item.cart.update_totals()
    return {'status': 'success', 'new_total': cart_item.cart.total_price}

@cart_bp.route('/remove_item/<int:id>')
@login_required
def remove_item(id):
    cart_item = CartItem.query.get_or_404(id)
    if cart_item.cart.user_id != current_user.id:
        flash('You do not have permission to remove this item.', 'danger')
        return redirect(url_for('cart.home'))
    
    cart = cart_item.cart
    db.session.delete(cart_item)
    db.session.commit()

    cart.update_totals()  # Cập nhật lại tổng số lượng và tổng giá của giỏ hàng
    db.session.commit()
    flash('Item removed from cart.', 'success')
    return redirect(url_for('cart.home'))