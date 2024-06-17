import React, { useState, useEffect } from 'eact';
import axios from 'axios';

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
    </div>
  );
}

export default App;













