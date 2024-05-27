from flask import Blueprint, render_template, request, redirect, url_for

checkout_bp = Blueprint('checkout', __name__)

@checkout_bp.route('/checkout')
def checkout():
    return render_template("checkout.html")

@checkout_bp.route('/process')
def process():
    name = request.form.get('name')
    address = request.form.get('address')
    phone = request.form.get('phone')
    print(name, address, phone)    
    return redirect(url_for('checkout.checkout'))