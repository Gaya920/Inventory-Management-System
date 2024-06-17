CREATE DATABASE 'Inventory-Management-System';
USE 'Inventory-Management-System';

# products table
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    unit_price REAL NOT NULL,
    supplier_id INTEGER NOT NULL,
    FOREIGN KEY(supplier_id) REFERENCES suppliers(id)
);

# suppliers table
CREATE TABLE suppliers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    contact TEXT NOT NULL,
    address TEXT NOT NULL
);

# warehouses table
CREATE TABLE warehouses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL
);

# stock_levels table
CREATE TABLE stock_levels (
    id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    warehouse_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY(product_id) REFERENCES products(id),
    FOREIGN KEY(warehouse_id) REFERENCES warehouses(id)
);
