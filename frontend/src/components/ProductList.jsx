import ProductCard from "./ProductCard";
import productsData from "../data/products.json";

const ProductList = () => {
  return (
    <div>
      <h2>Danh sách sản phẩm</h2>

      {productsData.map((product) => (
        <ProductCard
          key={product.id}
          product={product}
        />
      ))}
    </div>
  );
};

export default ProductList;