import React, { useState, useEffect } from 'eact';
import axios from 'axios';
import BarcodeScanner from './BarcodeScanner';

function App() {
  const [products, setProducts] = useState([]);
  const [selectedProduct, setSelectedProduct] = useState(null);

  useEffect(() => {
    axios.get('/api/products')
     .then(response => {
        setProducts(response.data);
      })
     .catch(error => {
       console.error(error);
      });
  }, []);

  const handleAddProduct = () => {
    // Implement add product functionality
  };

  const handleEditProduct = () => {
    // Implement edit product functionality
  };
  const handleDeleteProduct = () => {
    // Implement delete product functionality
  };

  const handleSelectProduct = (product) => {
    setSelectedProduct(product);
  };

  const handleScanBarcode = (barcode) => {
    // Use the scanned barcode to update the inventory management system
    axios.get(`/api/products/${barcode}`)
     .then(response => {
        const product = response.data;
        // Update stock levels accordingly
        axios.put(`/api/products/${product.id}`, { stock_level: product.stock_level - 1 })
         .then(response => {
            console.log(response.data);
           })
         .catch(error => {
            console.error(error);
          });
      })
     .catch(error => {
        console.error(error);
      });
  };
  return (
    <div>
      <h1>Inventory Management System</h1>
      <button onClick={handleAddProduct}>Add Product</button>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Description</th>
            <th>Category</th>
            <th>Unit Price</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {products.map((product) => (
            <tr key={product.id}>
              <td>{product.id}</td>
              <td>{product.name}</td>
              <td>{product.description}</td>
              <td>{product.category}</td>
              <td>{product.unit_price}</td>
              <td>
                <button onClick={() => handleEditProduct(product)}>Edit</button>
                <button onClick={() => handleDeleteProduct(product)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {selectedProduct && (
        <div>
          <h2>Product Details</h2>
          <p>ID: {selectedProduct.id}</p>
          <p>Name: {selectedProduct.name}</p>
          <p>Description: {selectedProduct.description}</p>
          <p>Category: {selectedProduct.category}</p>
          <p>Unit Price: {selectedProduct.unit_price}</p>
        </div>
      )}
      <BarcodeScanner onScan={handleScanBarcode} />
    </div>
  );
}

export default BarcodeScanner;
