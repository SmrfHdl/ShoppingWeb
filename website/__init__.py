from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'alonewolfs'

    from .views import views
    from .account import account_bp
    from .about import about
    from .cart import cart
    from .contact import contact
    from .pd import pd
    from .products import products

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(account_bp, url_prefix='/')
    app.register_blueprint(about, url_prefix='/')
    app.register_blueprint(cart, url_prefix='/')
    app.register_blueprint(contact, url_prefix='/')
    app.register_blueprint(pd, url_prefix='/')
    app.register_blueprint(products, url_prefix='/')

    return app