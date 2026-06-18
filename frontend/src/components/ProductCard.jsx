const ProductCard = ({ product }) => {
  return (
    <div
      style={{
        border: "1px solid #ccc",
        padding: "10px",
        margin: "10px",
        borderRadius: "8px",
      }}
    >
      <h3>{product.name}</h3>
      <p>Price: {product.price} VND</p>
    </div>
  );
};

export default ProductCard;