from flask_login import UserMixin
from datetime import datetime
from website import db

class User_Checkout(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    name = db.Column(db.String(150))  
    address = db.Column(db.String(300))  
    phone = db.Column(db.String(20))  
    balance = db.Column(db.Float, nullable=False, default=100000)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    name = db.Column(db.String(150), default = 'Lorem Ipsum')  
    address = db.Column(db.String(300), default = 'Lorem Ipsum Address')  
    phone = db.Column(db.String(20) , default= '0987654321')  
    balance = db.Column(db.Float, nullable=False, default=100000)

    orders = db.relationship("Order", back_populates="user")

    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=True)
    cart = db.relationship('Cart', backref=db.backref('users', lazy=True), foreign_keys=[cart_id])

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review_count = db.Column(db.Integer)
    description = db.Column(db.String(1000))
    image = db.Column(db.String(150), nullable=False)
    url = db.Column(db.String(300), nullable=False)
    category = db.Column(db.String(150), nullable=False)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_quantity = db.Column(db.Integer, nullable=False, default=0)
    total_price = db.Column(db.Integer, nullable=False, default=0)
    items = db.relationship('CartItem', backref='cart', lazy=True) 

    def update_totals(self):
        self.total_quantity = sum(item.quantity for item in self.items)
        self.total_price = sum(item.quantity * item.product.price for item in self.items)
        db.session.commit()

class CartItem(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False) 
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False) 
    size = db.Column(db.String(5))
    quantity = db.Column(db.Integer, nullable=False, default=1) 
    product = db.relationship('Product')

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False, default='Pending')
    total_price = db.Column(db.Float, nullable=False, default=0.0)

    items = db.relationship('OrderItem', backref='order', lazy=True)
    user = db.relationship("User", back_populates="orders")

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    size = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False, default='Completed')

