from flask import Flask, render_template, g, abort, request, jsonify
import sqlite3

app = Flask(__name__)

# Route cho trang chủ
@app.route('/')
def home():
    return render_template('index.html')

# Route cho Shop
@app.route('/shop')
def shop():
    return render_template('shop.html')

# Route cho Giỏ hàng
@app.route('/cart')
def cart():
    return render_template('cart.html')

# Route cho About
@app.route('/about')
def about():
    return render_template('about.html')

# Route cho Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route cho Account
@app.route('/account')
def account():
    return render_template('account.html')

# Route cho Thông tin chi tiết sản phẩm
@app.route('/product-detail')
def product_detail():
    return render_template('product-detail.html')


if __name__ == '__main__':
    app.run(debug=True)