from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'alonewolfs'

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

    return app