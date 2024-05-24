from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'alonewolfs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

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

    from .models import User, Product

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')