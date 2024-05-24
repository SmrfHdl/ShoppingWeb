from website import create_app, db
from website.models import Product

app = create_app()

with app.app_context():
    # Tạo một số sản phẩm mẫu
    products = [
        Product(name="Gift Card", price=100, description="Description for Product 1", image="https://assets-global.website-files.com/6644881a99e1e50c056f0640/6644881a99e1e50c056f06b4_acme-gift-card.jpg"),
        Product(name="Tin Coffee Tumbler", price=200, description="Description for Product 2", image="https://assets-global.website-files.com/6644881a99e1e50c056f0640/6644881a99e1e50c056f067d_ryan-holloway-JyDmUaXMib4-unsplash.jpg"),
        Product(name="Blue Canvas Pack", price=300, description="Description for Product 3", image="https://assets-global.website-files.com/6644881a99e1e50c056f0640/6644881a99e1e50c056f0669_denisse-leon-J7CjWufjmg4-unsplash.jpg"),
        Product(name="Green Canvas Pack", price=400, description="Description for Product 4", image="https://assets-global.website-files.com/6644881a99e1e50c056f0640/6644881a99e1e50c056f0646_jakob-owens-O_bhy3TnSYU-unsplash.jpg")
    ]

    # Thêm các sản phẩm vào phiên (session)
    db.session.add_all(products)
    
    # Lưu các thay đổi vào cơ sở dữ liệu
    db.session.commit()

    for product in products:
        print(f"Added product: {product.name}, Price: ${product.price}, Description: {product.description}, Image: {product.image}")

    print("Added sample products to the database!")
