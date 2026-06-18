import { useState } from "react";
import ProductCard from "./ProductCard";
import productsData from "../data/products.json";

const ProductList = () => {
  const [search, setSearch] = useState("");
  const [category, setCategory] = useState("All");
  const [sort, setSort] = useState("");

  let filteredProducts = productsData.filter((product) => {
    const matchName = product.name
      .toLowerCase()
      .includes(search.toLowerCase());

    const matchCategory =
      category === "All" ||
      product.category === category;

    return matchName && matchCategory;
  });

  if (sort === "asc") {
    filteredProducts.sort(
      (a, b) => a.price - b.price
    );
  }

  if (sort === "desc") {
    filteredProducts.sort(
      (a, b) => b.price - a.price
    );
  }

  return (
    <div>
      <h2>Product Catalog</h2>

      <input
        type="text"
        placeholder="Search product..."
        value={search}
        onChange={(e) =>
          setSearch(e.target.value)
        }
      />

      <br />
      <br />

      <select
        value={category}
        onChange={(e) =>
          setCategory(e.target.value)
        }
      >
        <option value="All">All</option>
        <option value="Phone">Phone</option>
        <option value="Laptop">Laptop</option>
      </select>

      <br />
      <br />

      <select
        value={sort}
        onChange={(e) =>
          setSort(e.target.value)
        }
      >
        <option value="">Default</option>
        <option value="asc">
          Price Low → High
        </option>
        <option value="desc">
          Price High → Low
        </option>
      </select>

      <hr />

      {filteredProducts.map((product) => (
        <ProductCard
          key={product.id}
          product={product}
        />
      ))}
    </div>
  );
};

export default ProductList;