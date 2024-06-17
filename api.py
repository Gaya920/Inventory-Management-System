from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///inventory.db"
db = SQLAlchemy(app)

#product API endpoints
@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])
  @app.route("/products/<int:product_id>", methods=["GET"])

def get_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product.to_dict())

@app.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()
    product = Product(name=data["name"], description=data["description"], unit_price=data["unit_price"], supplier_id=data["supplier_id"])
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    data = request.get_json()
    product.name = data["name"]
    product.description = data["description"]
    product.unit_price = data["unit_price"]
    db.session.commit()
    return jsonify(product.to_dict())

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Warehouse deleted"})

# Warehouses API endpoints
@app.route("/warehouses", methods=["GET"])
def get_warehouses():
    warehouses = Warehouse.query.all()
    return jsonify([warehouse.to_dict() for warehouse in warehouses])

@app.route("/warehouses/<int:warehouse_id>", methods=["GET"])
def get_warehouse(warehouse_id):
    warehouse = Warehouse.query.get(warehouse_id)
    if warehouse is None:
        return jsonify({"error": "Warehouse not found"}), 404
    return jsonify(warehouse.to_dict())@app.route("/warehouses", methods=["POST"])
  
def create_warehouse():
    data = request.get_json()
    warehouse = Warehouse(name=data["name"], location=data["location"])
    db.session.add(warehouse)
    db.session.commit()
    return jsonify(warehouse.to_dict()), 201

@app.route("/warehouses/<int:warehouse_id>", methods=["PUT"])
def update_warehouse(warehouse_id):
    warehouse = Warehouse.query.get(warehouse_id)
    if warehouse is None:
        return jsonify({"error": "Warehouse not found"}), 404
    data = request.get_json()
    warehouse.name = data["name"]
    warehouse.location = data["location"]
  db.session.commit()
    return jsonify(warehouse.to_dict())

@app.route("/warehouses/<int:warehouse_id>", methods=["DELETE"])
def delete_warehouse(warehouse_id):
    warehouse = Warehouse.query.get(warehouse_id)
    if warehouse is None:
        return jsonify({"error": "Warehouse not found"}), 404
    db.session.delete(warehouse)
    db.session.commit()
    return jsonify({"message": "Warehouse deleted"})

# Stock Levels API endpoints
@app.route("/stock_levels", methods=["GET"])
def get_stock_levels():
    stock_levels = StockLevel.query.all()
    return jsonify([stock_level.to_dict() for stock_level in stock_levels])

@app.route("/stock_levels/<int:stock_level_id>", methods=["GET"])
def get_stock_level(stock_level_id):
    stock_level = StockLevel.query.get(stock_level_id)
    if stock_level is None:
        return jsonify({"error": "Stock level not found"}), 404
    return jsonify(stock_level.to_dict())

@app.route("/stock_levels", methods=["POST"])
def create_stock_level():
    data = request.get_json()
    stock_level = StockLevel(product_id=data["product_id"], warehouse_id=data["warehouse_id"], quantity=data["quantity"])
    db.session.add(stock_level)
    db.session.commit()
    return jsonify(stock_level.to_dict()), 201

@app.route("/stock_levels/<int:stock_level_id>", methods=["PUT"])
def update_stock_level(stock_level_id):
    stock_level = StockLevel.query.get(stock_level_id)
    if stock_level is None:
        return jsonify({"error": "Stock level not found"}), 404
    data = request.get_json()
    stock_level.product_id = data["product_id"]
    stock_level.warehouse_id = data["warehouse_id"]
    stock_level.quantity = data["quantity"]
    db.session.commit()
    return jsonify(stock_level.to_dict())
  
@app.route("/stock_levels/<int:stock_level_id>", methods=["DELETE"])
def delete_stock_level(stock_level_id):
    stock_level = StockLevel.query.get(stock_level_id)
    if stock_level is None
