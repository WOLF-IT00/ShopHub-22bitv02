import { Link } from "react-router-dom";


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

      <p>
        Price: {product.price} VND
      </p>


      <Link to={`/products/${product.id}`}>
        View Detail
      </Link>


    </div>
  );
};


export default ProductCard;

