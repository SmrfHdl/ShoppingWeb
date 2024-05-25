from website import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))

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
    def update_total_quantity(self): 
        self.total_quantity = sum(item.quantity for item in self.items) 
        db.session.commit()

class CartItem(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False) 
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False) 
    quantity = db.Column(db.Integer, nullable=False, default=1) 