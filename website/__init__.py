from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
DB_NAME = "database.db"

class UserModelView(ModelView):
    column_list = ('id', 'email', 'password','username')

class ProductModelView(ModelView):
    column_list = ('id', 'name', 'price', 'rating', 'review_count', 'description', 'image', 'category')

class CartModelView(ModelView):
    column_list = ('id', 'user_id', 'total_quantity', 'total_price')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'alonewolfs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}?timeout=15'
    db.init_app(app)
    admin = Admin(app)

    from .views import views
    from .account import account_bp
    from .about import about_bp
    from .cart import cart_bp
    from .contact import contact_bp
    from .pd import pd_bp
    from .products import products_bp

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(account_bp, url_prefix='/')
    app.register_blueprint(about_bp, url_prefix='/')
    app.register_blueprint(cart_bp, url_prefix='/')
    app.register_blueprint(contact_bp, url_prefix='/')
    app.register_blueprint(pd_bp, url_prefix='/')
    app.register_blueprint(products_bp, url_prefix='/')

    from .models import User, Product, Cart

    admin.add_view(UserModelView(User, db.session))
    admin.add_view(ProductModelView(Product, db.session))
    admin.add_view(CartModelView(Cart, db.session, endpoint='admin_cart'))

    create_database(app)

    login_manager = LoginManager()
    # login_manager.login_view = 'account.home'
    login_manager.init_app(app)

    @login_manager.user_loader
    def login_manager(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')